# Generated by Django 5.0.6 on 2024-05-27 15:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Apply', '0002_remove_application_document'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Application',
            new_name='Profile',
        ),
    ]
