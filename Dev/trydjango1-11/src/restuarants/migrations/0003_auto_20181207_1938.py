# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-12-07 14:08
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