# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 06:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20171109_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCode',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='직급 코드')),
                ('codename', models.CharField(max_length=5, verbose_name='직급명')),
                ('sort', models.IntegerField(unique=True, verbose_name='순서')),
            ],
            options={
                'db_table': 'user_code',
            },
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='활성화 여부'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserCode', verbose_name='직급'),
        ),
    ]
