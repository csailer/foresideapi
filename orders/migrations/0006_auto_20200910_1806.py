# Generated by Django 3.1.1 on 2020-09-10 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderstatus',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='orders.order'),
        ),
    ]
