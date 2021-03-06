# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-09-28 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cpu',
            fields=[
                ('cID', models.AutoField(primary_key=True, serialize=False)),
                ('percent_util_cpu', models.FloatField()),
                ('time_cpu', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mem',
            fields=[
                ('mID', models.AutoField(primary_key=True, serialize=False)),
                ('percent_util_mem', models.FloatField()),
                ('time_mem', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
