# Generated by Django 5.0.6 on 2024-05-25 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]