# Generated by Django 3.2 on 2021-05-20 09:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0002_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='privateme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reciever', models.CharField(max_length=100, null=True)),
                ('msg', models.TextField()),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communication.registration')),
            ],
        ),
    ]
