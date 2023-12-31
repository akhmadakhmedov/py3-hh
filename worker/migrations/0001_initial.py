# Generated by Django 4.2.2 on 2023-07-02 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('specialisation', models.CharField(max_length=100, verbose_name='специализация')),
                ('expectated_salary', models.IntegerField()),
                ('is_searching', models.BooleanField()),
            ],
        ),
    ]
