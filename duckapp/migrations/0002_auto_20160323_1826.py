# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duckapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(blank=True, to='duckapp.Tag'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]