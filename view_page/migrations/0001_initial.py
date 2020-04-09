# Generated by Django 3.0.5 on 2020-04-07 04:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_date', models.DateField(default=django.utils.timezone.now)),
                ('log_time', models.TimeField(default=django.utils.timezone.now)),
                ('log_userid', models.CharField(max_length=60)),
                ('log_question', models.TextField(default='질문')),
                ('log_answer', models.TextField(default='답변')),
            ],
        ),
    ]
