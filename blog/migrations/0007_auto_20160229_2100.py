# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-29 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160226_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatpage',
            name='photo',
            field=models.ImageField(upload_to='new/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
    ]
