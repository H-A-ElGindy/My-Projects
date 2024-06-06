# Generated by Django 5.0.6 on 2024-05-27 11:31

import Courses.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('Hours', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('book', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=Courses.models.Course_image)),
            ],
            options={
                'verbose_name': 'Meeting',
                'verbose_name_plural': 'Meetings',
            },
        ),
    ]
