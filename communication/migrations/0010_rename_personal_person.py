# Generated by Django 3.2 on 2021-05-22 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0009_alter_personal_group'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='personal',
            new_name='person',
        ),
    ]
