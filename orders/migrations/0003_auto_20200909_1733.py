# Generated by Django 3.1.1 on 2020-09-09 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200909_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Date')),
                ('created_by', models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='Created By')),
                ('modified_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Modified Date')),
                ('modified_by', models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='Modified By')),
                ('status', models.CharField(choices=[('new', 'New Order'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='new', max_length=10, null=True, verbose_name='Order Status')),
                ('reason', models.CharField(blank=True, max_length=255, null=True, verbose_name='Reason')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
