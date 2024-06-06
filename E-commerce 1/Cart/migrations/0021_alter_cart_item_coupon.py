# Generated by Django 5.0.3 on 2024-04-18 14:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0020_remove_order_coupon_cart_item_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_item',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Cart.coupon'),
        ),
    ]
