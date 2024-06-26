# Generated by Django 5.0.3 on 2024-04-04 14:22

import Accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_alter_profile_image_alter_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default=1, upload_to=Accounts.models.user_image),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
