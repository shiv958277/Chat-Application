# Generated by Django 3.2 on 2021-05-25 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0011_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='r',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
