# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 17:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='album_tutle',
            new_name='album_title',
        ),
    ]