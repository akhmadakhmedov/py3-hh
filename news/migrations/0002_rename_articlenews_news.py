# Generated by Django 4.2.4 on 2023-08-08 21:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ArticleNews',
            new_name='News',
        ),
    ]