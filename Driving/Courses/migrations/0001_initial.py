# Generated by Django 5.0.6 on 2024-05-23 14:48

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
                ('name', models.CharField(max_length=50)),
                ('level', models.CharField(max_length=50)),
                ('Duration', models.IntegerField()),
                ('duration_type', models.CharField(choices=[('Months', 'Months'), ('Weeks', 'Weeks'), ('Days', 'Days')], max_length=50)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('is_available', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
    ]
