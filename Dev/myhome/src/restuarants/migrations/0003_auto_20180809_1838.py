# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-09 13:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restuarants', '0002_restuarant_location'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Restuarant',
            new_name='RestuarantLocation',
        ),
    ]
