# Generated by Django 4.2.4 on 2023-08-10 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_newsviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsviews',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]