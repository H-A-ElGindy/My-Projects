# Generated by Django 5.0.3 on 2024-04-18 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0006_product_offerprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='offerprice',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
