# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_song_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(max_length=1000, upload_to=''),
        ),
    ]
