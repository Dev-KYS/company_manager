# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-09 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacation',
            name='first_approval',
            field=models.CharField(default='', max_length=2, verbose_name='첫 승인 여부'),
        ),
        migrations.AlterField(
            model_name='vacation',
            name='last_approval',
            field=models.CharField(default='', max_length=2, verbose_name='마지막 승인 여부'),
        ),
    ]
