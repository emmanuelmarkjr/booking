# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-08 05:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersphones', '0017_movies_movie_pop_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviesperformances',
            name='movie_location',
            field=models.CharField(default='', max_length=250),
        ),
    ]
