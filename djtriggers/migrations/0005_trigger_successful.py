# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-08-24 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djtriggers', '0004_auto_20170216_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='trigger',
            name='successful',
            field=models.NullBooleanField(default=None),
        ),
    ]
