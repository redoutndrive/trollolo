# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 12:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20171109_1247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='activeStatus',
            new_name='status',
        ),
    ]
