# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-14 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0006_auto_20160614_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='display',
            field=models.CharField(default='s', max_length=30),
            preserve_default=False,
        ),
    ]
