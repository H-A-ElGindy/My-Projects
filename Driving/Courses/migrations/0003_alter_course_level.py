# Generated by Django 5.0.6 on 2024-05-23 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0002_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('Beginner', 'Begiinger'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], max_length=50),
        ),
    ]
