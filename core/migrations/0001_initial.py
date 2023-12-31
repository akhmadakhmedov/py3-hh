# Generated by Django 4.2.2 on 2023-07-01 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(default='No details')),
                ('is_relevant', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=254)),
                ('contacts', models.CharField(max_length=100, verbose_name='Kontakti')),
            ],
        ),
    ]
