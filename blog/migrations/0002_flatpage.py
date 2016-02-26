# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-17 23:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0001_initial'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlatPage',
            fields=[
                ('flatpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='flatpages.FlatPage')),
                ('Photo', models.ImageField(blank=True, upload_to='static/images')),
            ],
            bases=('flatpages.flatpage',),
        ),
    ]