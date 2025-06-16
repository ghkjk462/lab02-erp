
from django.utils import timezone

from apps.sales.models import SalesOrder, SalesGoods
from .models import DashboardStatistics
from apps.system.models import Team
from django.db import transaction, connection
from django.core.cache import cache  
from django.db.models import (
    Count, Sum, Q, F, Value, 
    DecimalField as AmountField  # 添加金额字段类型
)
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.functions import Coalesce  
from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task
def update_dashboard_statistics():
    """更新数据看板统计"""
    try:
        # 使用 timezone-aware 的时间
        today_start = timezone.make_aware(
            timezone.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        )
        tomorrow_start = today_start + timezone.timedelta(days=1)
        seven_days_ago = today_start - timezone.timedelta(days=7)
        logger.debug(f"统计时间范围: {today_start} - {tomorrow_start}\n")
        # 遍历所有团队更新统计
        for team in Team.objects.all():
            try: 
                with transaction.atomic():
                    stats, _ = DashboardStatistics.objects.get_or_create(team=team)
                    
                    # 1. 更新销售数据
                    sales_data = SalesOrder.objects.filter(
                        create_time__range=(today_start, tomorrow_start),
                        is_void=False,
                        team=team
                    ).aggregate(
                        sales_count=Count('id'),
                        sales_amount=Sum('total_amount')
                    )
                    stats.sales_count = sales_data['sales_count'] or 0
                    stats.sales_amount = sales_data['sales_amount'] or 0
                    
                    # 2. 更新采购数据
                    from apps.purchase.models import PurchaseOrder
                    purchase_data = PurchaseOrder.objects.filter(
                        create_time__range=(today_start, tomorrow_start),
                        is_void=False,
                        team=team
                    ).aggregate(
                        purchase_count=Count('id')
                    )
                    stats.purchase_count = purchase_data['purchase_count'] or 0
                    
                    # 3. 更新待办任务数据
                    from apps.stock_in.models import StockInOrder
                    from apps.stock_out.models import StockOutOrder
                    
                    # 待入库任务
                    stats.stock_in_task_count = StockInOrder.objects.filter(
                        is_completed=False,
                        is_void=False,
                        team=team
                    ).count()
                    
                    # 待出库任务
                    stats.stock_out_task_count = StockOutOrder.objects.filter(
                        is_completed=False,
                        is_void=False,
                        team=team
                    ).count()
                    
                    # 4. 更新库存预警数据
                    from apps.goods.models import Inventory
                    stats.inventory_warning_count = Inventory.objects.filter(
                        team=team,
                        goods__enable_inventory_warning=True
                    ).filter(
                        Q(total_quantity__lt=F('goods__inventory_lower')) |
                        Q(total_quantity__gt=F('goods__inventory_upper'))
                    ).count()
                    
                    # 5. 更新临期预警数据 - 从批次表中统计临期商品
                    from apps.goods.models import Batch
                    stats.expiration_warning_count = Batch.objects.filter(
                        team=team,
                        expiration_date__isnull=False,
                        expiration_date__lte=timezone.now() + timezone.timedelta(days=30),
                        has_stock=True  # 只统计有库存的批次
                    ).count()
                    
                    # 6. 更新欠款统计
                    from apps.data.models import Client, Supplier

                    # 应收欠款
                    receivable = Client.objects.filter(
                        team=team,
                        is_active=True,  # 只统计激活的客户
                        has_arrears=True  # 只统计有欠款的客户
                    ).aggregate(
                        total=Sum('arrears_amount')
                    )['total'] or 0
                    stats.arrears_receivable_amount = receivable

                    # 应付欠款
                    payable = Supplier.objects.filter(
                        team=team,
                        is_active=True,  # 只统计激活的供应商
                        has_arrears=True  # 只统计有欠款的供应商
                    ).aggregate(
                        total=Sum('arrears_amount')
                    )['total'] or 0
                    stats.arrears_payable_amount = payable


                    # 更新销售热销商品TOP10
                    hot_goods = SalesGoods.objects.filter(
                        sales_order__is_void=False,
                        sales_order__team=team
                    ).select_related('goods', 'goods__category', 'goods__unit'
                    ).values('goods').annotate(
                        goods_number=F('goods__number'),
                        goods_name=F('goods__name'),
                        goods_barcode=F('goods__barcode'),
                        goods_spec=F('goods__spec'),
                        category_name=F('goods__category__name'),
                        unit_name=F('goods__unit__name'),
                        total_sales_quantity=Coalesce(Sum('sales_quantity'), Value(0.0))
                    ).order_by('-total_sales_quantity')[:10]
                    
                     # 更新销售趋势 - 修改日期处理
                    sales_trend = list(SalesOrder.objects.filter(
                        is_void=False,
                        team=team
                    ).select_related('warehouse'
                    ).extra(
                        select={'date': connection.ops.date_trunc_sql('day', 'create_time')}
                    ).values('warehouse', 'date').annotate(
                        warehouse_number=F('warehouse__number'),
                        warehouse_name=F('warehouse__name'),
                        total_sales_amount=Coalesce(Sum('total_amount'), Value(0, output_field=AmountField()))
                    ))
                    
                    # 转换日期为字符串
                    for item in sales_trend:
                        if 'date' in item and item['date']:
                            item['date'] = item['date'].isoformat()
                        if 'total_sales_amount' in item:
                            item['total_sales_amount'] = str(item['total_sales_amount'])
                    
                    # 保存到模型
                    stats.hot_goods_data = list(hot_goods)
                    stats.sales_trend_data = sales_trend
                    stats.last_update = timezone.now()
                    stats.save()

                    # # 更新缓存 - 确保所有数据都是JSON可序列化的
                    # cache_data = {
                    #     'sales_count': stats.sales_count,
                    #     'sales_amount': str(stats.sales_amount),
                    #     'purchase_count': stats.purchase_count,
                    #     'stock_in_task_count': stats.stock_in_task_count,
                    #     'stock_out_task_count': stats.stock_out_task_count,
                    #     'inventory_warning_count': stats.inventory_warning_count,
                    #     'expiration_warning_count': stats.expiration_warning_count,
                    #     'arrears_receivable_amount': str(stats.arrears_receivable_amount),
                    #     'arrears_payable_amount': str(stats.arrears_payable_amount),
                    #     'hot_goods_data': stats.hot_goods_data,
                    #     'sales_trend_data': stats.sales_trend_data,
                    #     'last_update': stats.last_update.isoformat()
                    # }
                    
                    # cache.set(f'dashboard_stats_{team.id}', cache_data, 60)
                    
                    logger.info(f"团队 {team.number} 统计数据更新完成")
            except Exception as e:
                    logger.error(f"处理团队 {team.number} 时发生错误: {str(e)}")
                    continue
            
        return "Dashboard statistics updated successfully"
    except Exception as e:
        logger.error(f"更新数据看板统计时发生错误: {str(e)}")
        raise