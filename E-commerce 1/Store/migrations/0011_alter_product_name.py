# Generated by Django 5.0.3 on 2024-05-01 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0010_alter_offer_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
