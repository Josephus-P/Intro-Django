# Generated by Django 2.1.2 on 2018-10-23 23:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='note',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
