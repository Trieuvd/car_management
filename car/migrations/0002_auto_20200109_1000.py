# Generated by Django 2.2.9 on 2020-01-09 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='user_id',
            new_name='user',
        ),
    ]
