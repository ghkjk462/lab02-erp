# Generated by Django 3.2 on 2025-05-22 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('system', '0001_initial'),
        ('goods', '0001_initial'),
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=32, verbose_name='编号')),
                ('is_related', models.BooleanField(default=False, verbose_name='关联状态')),
                ('total_quantity', models.FloatField(verbose_name='生产总数')),
                ('quantity_produced', models.FloatField(verbose_name='已生产数量')),
                ('remain_quantity', models.FloatField(verbose_name='剩余数量')),
                ('start_time', models.DateTimeField(null=True, verbose_name='开始时间')),
                ('end_time', models.DateTimeField(null=True, verbose_name='结束时间')),
                ('status', models.CharField(choices=[('in_plan', '计划中'), ('in_progress', '进行中'), ('completed', '已完成'), ('closed', '强制关闭')], default='in_plan', max_length=32, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_production_orders', to='system.user', verbose_name='创建人')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='production_orders', to='goods.goods', verbose_name='产品')),
                ('sales_order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='production_orders', to='sales.salesorder', verbose_name='销售单')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='production_orders', to='system.team')),
            ],
        ),
        migrations.CreateModel(
            name='ProductionRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('production_quantity', models.FloatField(verbose_name='生产数量')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_production_records', to='system.user', verbose_name='创建人')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='production_records', to='goods.goods', verbose_name='产品')),
                ('production_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='production_records', to='production.productionorder', verbose_name='生产单')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='production_records', to='system.team')),
            ],
        ),
    ]
