# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-12-07 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restuarants', '0003_auto_20181207_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='restuarantlocation',
            name='category',
            field=models.CharField(max_length=120, null=True),
        ),
    ]