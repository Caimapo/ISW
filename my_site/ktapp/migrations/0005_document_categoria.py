# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-13 05:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ktapp', '0004_clasificar'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='categoria',
            field=models.CharField(default=b'nada', max_length=20),
        ),
    ]