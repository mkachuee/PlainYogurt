# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-07 18:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='treeinfo',
            old_name='topicx',
            new_name='topic',
        ),
    ]
