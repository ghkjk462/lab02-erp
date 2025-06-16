from django.db import models
from extensions.models import Model

class DashboardStatistics(Model):
    """数据看板统计"""
    team = models.ForeignKey('system.Team', on_delete=models.CASCADE, related_name='dashboard_statistics')
    
    # 今日数据
    sales_count = models.IntegerField(default=0, verbose_name='今日销售笔数')
    sales_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='今日销售额')
    purchase_count = models.IntegerField(default=0, verbose_name='今日采购笔数')
    
    # 待办任务
    stock_in_task_count = models.IntegerField(default=0, verbose_name='待入库数')
    stock_out_task_count = models.IntegerField(default=0, verbose_name='待出库数')
    inventory_warning_count = models.IntegerField(default=0, verbose_name='库存预警数')
    expiration_warning_count = models.IntegerField(default=0, verbose_name='临期预警数')
    
    # 欠款统计
    arrears_receivable_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='应收欠款')
    arrears_payable_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='应付欠款')

    sales_trend_data = models.JSONField(default=dict, verbose_name='销售走势数据')
    hot_goods_data = models.JSONField(default=dict, verbose_name='热销商品数据')
    
    last_update = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')

    class Meta:
        verbose_name = '数据看板统计'
        verbose_name_plural = verbose_name
        unique_together = [('team',)]

    def __str__(self):
        return f"{self.team.name} - 数据看板统计"

__all__ = [
    'DashboardStatistics'
]
