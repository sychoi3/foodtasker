# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-18 03:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0006_auto_20170618_0154'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='location',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
