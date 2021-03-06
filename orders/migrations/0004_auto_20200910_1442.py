# Generated by Django 3.1.1 on 2020-09-10 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200909_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='client',
            field=models.CharField(max_length=150, null=True, verbose_name='Client'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('cash', 'Cash'), ('kind', 'Kind')], default='cash', max_length=10, null=True, verbose_name='Payment Method'),
        ),
        migrations.AddField(
            model_name='order',
            name='transaction_type',
            field=models.CharField(choices=[('create', 'Create'), ('redeem', 'Redeem')], default='create', max_length=10, null=True, verbose_name='Transaction Type'),
        ),
    ]
