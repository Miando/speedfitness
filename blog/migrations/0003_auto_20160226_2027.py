# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-26 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_flatpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatpage',
            name='Photo',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
