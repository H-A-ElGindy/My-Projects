# Generated by Django 5.1 on 2024-08-27 16:45

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='C:/Users/aelgi/Desktop/Power Zone/power-zone/static/img/empty.jpg', null=True, upload_to=accounts.models.profile_image),
        ),
    ]
