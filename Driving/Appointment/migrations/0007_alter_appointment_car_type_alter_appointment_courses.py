# Generated by Django 5.0.6 on 2024-05-25 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appointment', '0006_alter_appointment_car_type_alter_appointment_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='car_type',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='courses',
            field=models.CharField(max_length=150),
        ),
    ]
