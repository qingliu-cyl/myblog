# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2019-01-11 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sg', '0003_auto_20190111_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sgflag',
            name='flag',
            field=models.TextField(null=True),
        ),
    ]
