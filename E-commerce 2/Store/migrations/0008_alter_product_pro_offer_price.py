# Generated by Django 5.0.6 on 2024-05-21 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0007_alter_product_pro_offer_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pro_offer_price',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
