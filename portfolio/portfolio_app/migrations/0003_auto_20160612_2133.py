# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-12 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_auto_20160612_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(max_length=500),
        ),
    ]
