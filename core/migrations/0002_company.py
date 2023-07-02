# Generated by Django 4.2.2 on 2023-07-02 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField(default='Address does not shown')),
                ('staff_quantity', models.IntegerField()),
                ('is_hunting', models.BooleanField(default=False)),
            ],
        ),
    ]
