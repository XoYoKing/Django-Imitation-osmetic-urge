# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-10 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20180110_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='novel_name',
            field=models.IntegerField(default=0, verbose_name='小说ID'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='user_name',
            field=models.IntegerField(default=0, verbose_name='用户ID'),
        ),
        migrations.AlterField(
            model_name='readnovel',
            name='novel_name',
            field=models.IntegerField(default=0, verbose_name='小说ID'),
        ),
        migrations.AlterField(
            model_name='readnovel',
            name='user_name',
            field=models.IntegerField(default=0, verbose_name='用户ID'),
        ),
    ]
