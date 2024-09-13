# Generated by Django 5.1 on 2024-08-23 14:52

import accounts.models
import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Coach',
                'verbose_name_plural': 'Coaches',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_slug', models.SlugField(blank=True, null=True, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('facebook', models.URLField(blank=True, max_length=2000, null=True, unique=True)),
                ('linkedin', models.URLField(blank=True, max_length=2000, null=True, unique=True)),
                ('phone', models.CharField(blank=True, max_length=11, null=True, unique=True)),
                ('designation', models.CharField(max_length=50)),
                ('rating_total', models.DecimalField(blank=True, decimal_places=1, max_digits=1, null=True)),
                ('rating_number', models.IntegerField(blank=True, null=True)),
                ('average_rating', models.DecimalField(blank=True, decimal_places=1, max_digits=1, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=accounts.models.profile_image)),
                ('biography', models.TextField(blank=True, null=True)),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
                ('is_available', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('post_slug', models.SlugField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to=accounts.models.post_file)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
