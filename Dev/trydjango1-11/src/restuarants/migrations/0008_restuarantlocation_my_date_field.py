# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-12-14 11:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restuarants', '0007_auto_20181214_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='restuarantlocation',
            name='my_date_field',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]