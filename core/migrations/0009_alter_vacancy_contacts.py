# Generated by Django 4.2.2 on 2023-07-11 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_vacancy_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='contacts',
            field=models.CharField(max_length=100, verbose_name='Контакты'),
        ),
    ]