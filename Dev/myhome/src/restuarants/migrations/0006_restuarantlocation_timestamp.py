# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-11 12:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restuarants', '0005_auto_20180811_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='restuarantlocation',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]