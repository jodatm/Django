# Generated by Django 2.0.6 on 2018-06-27 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='jobs',
            new_name='Job',
        ),
    ]
