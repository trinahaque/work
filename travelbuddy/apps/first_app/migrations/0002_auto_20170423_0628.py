# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-23 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='joiner',
            field=models.ManyToManyField(related_name='joiner', to='first_app.User'),
        ),
    ]
