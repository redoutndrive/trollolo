# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20171115_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='archiveStatus',
            field=models.BooleanField(default=False),
        ),
    ]
