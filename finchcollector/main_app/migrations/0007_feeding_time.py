# Generated by Django 5.0.2 on 2024-03-13 03:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_feeding_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeding',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
