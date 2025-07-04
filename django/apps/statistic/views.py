from extensions.common.schema import *
from extensions.common.base import *
from extensions.permissions import *
from extensions.exceptions import *
from extensions.viewsets import *
from extensions.models import *
from apps.statistic.serializers import *
from apps.statistic.permissions import *
from apps.statistic.filters import *
from apps.statistic.schemas import *
from apps.statistic.models import *
from apps.purchase.models import *
from apps.sales.models import *
from apps.finance.models import *
from apps.stock_in.models import *
from apps.stock_out.models import *
from apps.goods.models import *
from apps.data.models import *
from django.db import connection
from django.utils import timezone


class PurchaseReportViewSet(BaseViewSet):
    """采购报表"""

    permission_classes = [IsAuthenticated, PurchaseReportPermission]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = PurchaseReportFilter
    search_fields = ['goods__number', 'goods__name']
    queryset = PurchaseGoods.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(purchase_order__is_void=False)

    @extend_schema(parameters=[PurchaseReportParameter],
                   responses={200: PurchaseReportStatisticResponse})
    @action(detail=False, methods=['get'])
    def statistics(self, request, *args, **kwargs):
        """统计"""

        queryset = self.filter_queryset(self.get_queryset())
        result = queryset.aggregate(
            total_count=Count('purchase_order', distinct=True),
            total_quantity=Coalesce(Sum('purchase_quantity'), Value(0.0)),
            total_amount=Coalesce(Sum('total_amount'), Value(0, output_field=AmountField()))
        )

        return Response(data=result, status=status.HTTP_200_OK)

    @extend_schema(parameters=[PurchaseReportParameter],
                   responses={200: PurchaseReportDetialSerializer})
    @action(detail=False, methods=['get'])
    def detials(self, request, *args, **kwargs):
        """明细"""

        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.select_related('goods', 'goods__category', 'goods__unit', 'purchase_order',
                                           'purchase_order__warehouse', 'purchase_order__supplier',
                                           'purchase_order__creator')
        queryset = self.paginate_queryset(queryset)

        serializer = PurchaseReportDetialSerializer(instance=queryset, many=True)
        return self.get_paginated_response(serializer.data)

    @extend_schema(parameters=[PurchaseReportParameter],
                   responses={200: PurchaseReportGroupByGoodsResponse})
    @action(detail=False, methods=['get'])
    def group_by_goods(self, request, *args, **kwargs):
        """产品汇总"""

        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.select_related('goods', 'goods__category', 'goods__unit')
        queryset = queryset.values('goods').annotate(
            goods_number=F('goods__number'), goods_name=F('goods__name'),
            goods_barcode=F('goods__barcode'), goods_spec=F('goods__spec'),
            category_name=F('goods__category__name'), unit_name=F('goods__unit__name'),
            total_purchase_quantity=Coalesce(Sum('purchase_quantity'), Value(0.0)),
            total_purchase_amount=Coalesce(Sum('total_amount'), Value(0, output_field=AmountField())),
            min_purchase_price=Min('purchase_price'), avg_purchase_price=Avg('purchase_price'),
            max_purchase_price=Max('purchase_price')
        )
        queryset = self.paginate_queryset(queryset)

        return self.get_paginated_response(queryset)


class SalesReportViewSet(BaseViewSet):
    """销售报表"""

    permission_classes = [IsAuthenticated, SalesReportPermission]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = SalesReportFilter
    search_fields = ['goods__number', 'goods__name']
    queryset = SalesGoods.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(sales_order__is_void=False)

    @extend_schema(parameters=[SalesReportParameter],
                   responses={200: SalesReportStatisticResponse})
    @action(detail=False, methods=['get'])
    def statistics(self, request, *args, **kwargs):
        """统计"""

        queryset = self.filter_queryset(self.get_queryset())
        result = queryset.aggregate(
            total_count=Count('sales_order', distinct=True),
            total_quantity=Coalesce(Sum('sales_quantity'), Value(0.0)),
            total_amount=Coalesce(Sum('total_amount'), Value(0, output_field=AmountField()))
        )

        return Response(data=result, status=status.HTTP_200_OK)

    @extend_schema(parameters=[SalesReportParameter],
                   responses={200: SalesReportDetialSerializer})
    @action(detail=False, methods=['get'])
    def detials(self, request, *args, **kwargs):
        """明细"""

        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.select_related('goods', 'goods__category', 'goods__unit', 'sales_order',
                                           'sales_order__warehouse', 'sales_order__client',
                                           'sales_order__creator')
        queryset = self.paginate_queryset(queryset)

        serializer = SalesReportDetialSerializer(instance=queryset, many=True)
        return self.get_paginated_response(serializer.data)

    @extend_schema(parameters=[SalesReportParameter],
                   responses={200: SalesReportGroupByGoodsResponse})
    @action(detail=False, methods=['get'])
    def group_by_goods(self, request, *args, **kwargs):
        """产品汇总"""

        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.select_related('goods', 'goods__category', 'goods__unit')
        queryset = queryset.values('goods').annotate(
            goods_number=F('goods__number'), goods_name=F('goods__name'),
            goods_barcode=F('goods__barcode'), goods_spec=F('goods__spec'),
            category_name=F('goods__category__name'), unit_name=F('goods__unit__name'),
            total_sales_quantity=Coalesce(Sum('sales_quantity'), Value(0.0)),
            total_sales_amount=Coalesce(Sum('total_amount'), Value(0, output_field=AmountField())),
            min_sales_price=Min('sales_price'), avg_sales_price=Avg('sales_price'),
            max_sales_price=Max('sales_price')
        )
        queryset = self.paginate_queryset(queryset)

        return self.get_paginated_response(queryset)

class SalesHotGoodsViewSet(BaseViewSet, ListModelMixin):
    """销售前十产品"""
    
    @extend_schema(parameters=[SalesHotGoodsParameter], responses={200: SalesHotGoodsResponse})
    def list(self, request, *args, **kwargs):
        """根据日期范围获取销售前十产品"""
        serializer = SalesHotGoodsParameter(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        
        start_date = serializer.validated_data['start_date']
        end_date = serializer.validated_data['end_date']
        
        # 构建查询条件（使用相同的时区处理逻辑）
        query_filters = (
            Q(sales_order__create_time__gte=start_date) &
            Q(sales_order__create_time__lt=end_date) &
            Q(sales_order__is_void=False) & 
            Q(sales_order__team=self.team)
        )
        
        # 查询销售前十产品
        hot_goods = list(SalesGoods.objects.filter(query_filters)
            .select_related('goods', 'goods__category', 'goods__unit')
            .values('goods')
            .annotate(
                goods_number=F('goods__number'),
                goods_name=F('goods__name'),
                goods_barcode=F('goods__barcode'),
                goods_spec=F('goods__spec'),
                category_name=F('goods__category__name'),
                unit_name=F('goods__unit__name'),
                total_sales_quantity=Coalesce(Sum('sales_quantity'), Value(0.0))
            )
            .order_by('-total_sales_quantity')[:10])
        
        return Response(data=hot_goods, status=status.HTTP_200_OK)
    
class SalesTrendViewSet(BaseViewSet, ListModelMixin):
    """销售走势"""
    
    @extend_schema(parameters=[SalesTrendParameter], responses={200: SalesTrendResponse})
    def list(self, request, *args, **kwargs):
        """根据日期范围获取销售走势数据"""
        # 使用与销售报表相同的查询逻辑，确保数据一致性
        # 基于SalesOrder而不是SalesGoods，但使用相同的时间过滤逻辑
        
        serializer = SalesTrendParameter(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        
        start_date = serializer.validated_data['start_date']
        end_date = serializer.validated_data['end_date']
        
        # 使用Django过滤器的相同逻辑
        query_filters = (
            Q(create_time__gte=start_date) &
            Q(create_time__lt=end_date) &
            Q(is_void=False) & 
            Q(team=self.team)
        )
        
        # 按本地时区日期分组查询销售数据
        sales_trend = list(SalesOrder.objects.filter(query_filters)
            .extra(
                select={
                    'date': "DATE(CONVERT_TZ(create_time, '+00:00', '+08:00'))"
                }
            )
            .values('date')
            .annotate(
                total_sales_amount=Coalesce(Sum('total_amount'), Value(0, output_field=AmountField()))
            )
            .order_by('date'))
        
        # 转换日期为字符串格式
        for item in sales_trend:
            if 'date' in item and item['date']:
                item['date'] = item['date'].strftime('%Y-%m-%d')
            if 'total_sales_amount' in item:
                item['total_sales_amount'] = float(item['total_sales_amount'])
        
        return Response(data=sales_trend, status=status.HTTP_200_OK)

class FinanceStatisticViewSet(FunctionViewSet):
    """收支统计"""

    @extend_schema(parameters=[FinanceStatisticParameter], responses={200: FinanceStatisticResponse})
    def list(self, request, *args, **kwargs):
        serializer = FinanceStatisticParameter(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        query_filters = (
            Q(create_time__gte=serializer.data['start_date']) &
            Q(create_time__lt=serializer.data['end_date']) &
            Q(is_void=False) & Q(team=self.team)
        )

        result = {}
        result |= SalesOrder.objects.filter(query_filters).aggregate(
            total_sales_amount=Coalesce(Sum('total_amount'), Value(0, output_field=AmountField())))
        result |= SalesReturnOrder.objects.filter(query_filters).aggregate(
            total_sales_reutrn_amount=Coalesce(Sum('total_amount'), Value(0, output_field=AmountField())))
        result |= PurchaseOrder.objects.filter(query_filters).aggregate(
            total_purchase_amount=Coalesce(Sum('total_amount'), Value(0, output_field=AmountField())))
        result |= PurchaseReturnOrder.objects.filter(query_filters).aggregate(
            total_purchase_return_amount=Coalesce(Sum('total_amount'), Value(0, output_field=AmountField())))
        result |= ChargeOrder.objects.filter(query_filters).filter(type=ChargeOrder.Type.INCOME).aggregate(
            total_income_amount=Coalesce(Sum('total_amount'), Value(0, output_field=AmountField())))
        result |= ChargeOrder.objects.filter(query_filters).filter(type=ChargeOrder.Type.EXPENDITURE).aggregate(
            total_expenditure_amount=Coalesce(Sum('total_amount'), Value(0, output_field=AmountField())))

        return Response(data=result, status=status.HTTP_200_OK)


class PaymentOrderDetialViewSet(BaseViewSet, ListModelMixin):
    """付款明细"""

    serializer_class = PaymentOrderDetialSerializer
    permission_classes = [IsAuthenticated, FinanceStatisticPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PaymentOrderDetialFilter
    queryset = PaymentOrder.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(is_void=False)


class CollectionOrderDetialViewSet(BaseViewSet, ListModelMixin):
    """收款明细"""

    serializer_class = CollectionOrderDetialSerializer
    permission_classes = [IsAuthenticated, FinanceStatisticPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CollectionOrderDetialFilter
    queryset = CollectionOrder.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(is_void=False)


class IncomeChargeOrderDetialViewSet(BaseViewSet, ListModelMixin):
    """收入费用明细"""

    serializer_class = IncomeChargeOrderDetialSerializer
    permission_classes = [IsAuthenticated, FinanceStatisticPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_class = IncomeChargeOrderDetialFilter
    queryset = ChargeOrder.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(type=ChargeOrder.Type.INCOME, is_void=False)


class ExpenditureChargeOrderDetialViewSet(BaseViewSet, ListModelMixin):
    """支出费用明细"""

    serializer_class = ExpenditureChargeOrderDetialSerializer
    permission_classes = [IsAuthenticated, FinanceStatisticPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ExpenditureChargeOrderDetialFilter
    queryset = ChargeOrder.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(type=ChargeOrder.Type.EXPENDITURE, is_void=False)


class PurchasePaymentDetialViewSet(BaseViewSet, ListModelMixin):
    """采购付款明细"""

    serializer_class = PurchasePaymentDetialSerializer
    permission_classes = [IsAuthenticated, FinanceStatisticPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PurchasePaymentDetialFilter
    queryset = PurchaseOrder.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(is_void=False)


class PurchaseReturnCollectionDetialViewSet(BaseViewSet, ListModelMixin):
    """采购退货收款明细"""

    serializer_class = PurchaseReturnCollectionDetialSerializer
    permission_classes = [IsAuthenticated, FinanceStatisticPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PurchaseReturnCollectionDetialFilter
    queryset = PurchaseReturnOrder.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(is_void=False)


class SalesCollectionDetialViewSet(BaseViewSet, ListModelMixin):
    """销售收款明细"""

    serializer_class = SalesCollectionDetialSerializer
    permission_classes = [IsAuthenticated, FinanceStatisticPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SalesCollectionDetialFilter
    queryset = SalesOrder.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(is_void=False)


class SalesReturnPaymentDetialViewSet(BaseViewSet, ListModelMixin):
    """销售退货付款明细"""

    serializer_class = SalesReturnPaymentDetialSerializer
    permission_classes = [IsAuthenticated, FinanceStatisticPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SalesReturnPaymentDetialFilter
    queryset = SalesReturnOrder.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(is_void=False)
    

from django.core.cache import cache
from decimal import Decimal
from django.utils import timezone
class HomeOverviewViewSet(BaseViewSet, ListModelMixin):
    """首页概览"""

    # def get_cache_key(self):
    #     return f'dashboard_stats_{self.team.id}'
    
    @extend_schema(responses={200: HomeViewResponse})
    def list(self, request, *args, **kwargs):
        # 先尝试从缓存获取
        # cache_key = self.get_cache_key()
        # data = cache.get(cache_key)
        
        if True:
            # 缓存未命中,从数据库获取
            # 从统计表获取数据
            try:
                stats = DashboardStatistics.objects.get(team=self.team)
                data = {
                    "sales_count": stats.sales_count,
                    "sales_amount": stats.sales_amount,
                    "purchase_count": stats.purchase_count,
                    "stock_in_task_count": stats.stock_in_task_count,
                    "stock_out_task_count": stats.stock_out_task_count,
                    "inventory_warning_count": stats.inventory_warning_count,
                    "expiration_warning_count": stats.expiration_warning_count,
                    "arrears_receivable_amount": stats.arrears_receivable_amount,
                    "arrears_payable_amount": stats.arrears_payable_amount,
                    "last_update": stats.last_update,
                }
                # cache.set(cache_key, data, 60) # s
            except DashboardStatistics.DoesNotExist:
                # 如果没有统计数据,返回默认值
                data = {
                    "sales_count": 0,
                    "sales_amount": Decimal('0.00'),
                    "purchase_count": 0,
                    "stock_in_task_count": 0,
                    "stock_out_task_count": 0,
                    "inventory_warning_count": 0,
                    "expiration_warning_count": 0,
                    "arrears_receivable_amount": Decimal('0.00'),
                    "arrears_payable_amount": Decimal('0.00'),
                    "last_update": timezone.now()
                }

        return Response(data=data, status=status.HTTP_200_OK)


__all__ = [
    'PurchaseReportViewSet', 'SalesReportViewSet', 'SalesHotGoodsViewSet',
    'SalesTrendViewSet', 'FinanceStatisticViewSet',
    'PaymentOrderDetialViewSet', 'CollectionOrderDetialViewSet',
    'IncomeChargeOrderDetialViewSet', 'ExpenditureChargeOrderDetialViewSet',
    'PurchasePaymentDetialViewSet', 'PurchaseReturnCollectionDetialViewSet',
    'SalesCollectionDetialViewSet', 'SalesReturnPaymentDetialViewSet',
]
