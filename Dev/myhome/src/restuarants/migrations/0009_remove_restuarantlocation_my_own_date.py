# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-11 12:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restuarants', '0008_restuarantlocation_my_own_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restuarantlocation',
            name='my_own_date',
        ),
    ]
