# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersphones', '0006_auto_20170830_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='movie_code',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='movies',
            name='movie_title',
            field=models.CharField(default='', max_length=250),
        ),
    ]