# Generated by Django 5.0.6 on 2024-05-23 15:10

import Courses.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0005_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default=1, upload_to=Courses.models.course_image),
            preserve_default=False,
        ),
    ]
