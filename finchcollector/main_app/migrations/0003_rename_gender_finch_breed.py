# Generated by Django 5.0.2 on 2024-03-09 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_breed_finch_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='finch',
            old_name='gender',
            new_name='breed',
        ),
    ]
