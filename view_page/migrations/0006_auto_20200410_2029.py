# Generated by Django 3.0.5 on 2020-04-10 20:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('view_page', '0005_auto_20200410_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='log_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='log',
            name='log_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
