# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-06 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersphones', '0007_auto_20170905_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='movie_banner',
            field=models.ImageField(default='', upload_to='static/images/banners'),
        ),
    ]
