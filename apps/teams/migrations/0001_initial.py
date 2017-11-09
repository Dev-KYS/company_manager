# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 11:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('tid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='팀 고유 아이디')),
                ('name', models.CharField(max_length=20, verbose_name='팀 이름')),
                ('created', models.DateField(blank=True, null=True, verbose_name='팀 생성일')),
                ('members', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='팀 멤버')),
            ],
            options={
                'verbose_name': '팀',
                'verbose_name_plural': '팀들',
                'db_table': 'teams',
            },
        ),
    ]