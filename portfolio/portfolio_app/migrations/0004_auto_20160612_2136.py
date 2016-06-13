# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-12 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0003_auto_20160612_2133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='title',
            new_name='company',
        ),
        migrations.AddField(
            model_name='experience',
            name='description',
            field=models.CharField(default=None, max_length=1000),
            preserve_default=False,
        ),
    ]
