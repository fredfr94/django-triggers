# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 09:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [('djtriggers', '0001_initial'), ('djtriggers', '0002_auto_20151208_1454'), ('djtriggers', '0003_auto_20160512_0847'), ('djtriggers', '0004_auto_20170216_1007'), ('djtriggers', '0005_trigger_successful'), ('djtriggers', '0006_auto_20171003_0945')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trigger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trigger_type', models.CharField(db_index=True, max_length=50)),
                ('source', models.CharField(blank=True, max_length=250, null=True)),
                ('date_received', models.DateTimeField()),
                ('date_processed', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('process_after', models.DateTimeField(blank=True, db_index=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TriggerResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.TextField()),
                ('trigger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djtriggers.Trigger')),
            ],
        ),
        migrations.AlterField(
            model_name='trigger',
            name='date_received',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='trigger',
            name='source',
            field=models.CharField(blank=True, db_index=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='trigger',
            name='number_of_tries',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='trigger',
            name='date_received',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='trigger',
            name='successful',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='trigger',
            name='source',
            field=models.CharField(blank=True, db_index=True, max_length=150, null=True),
        ),
    ]
