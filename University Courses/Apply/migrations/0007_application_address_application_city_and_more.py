# Generated by Django 5.0.6 on 2024-05-29 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apply', '0006_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='address',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='city',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='phone',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='school',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
