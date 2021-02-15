# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-09 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("beaconsite", "0003_auto_20210304_1052"),
    ]

    operations = [
        migrations.AlterField(
            model_name="consortium",
            name="identifier",
            field=models.CharField(
                help_text="Identifier of consortium (e.g., in reverse DNS notation)",
                max_length=128,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="site",
            name="identifier",
            field=models.CharField(
                help_text="Site name (in reverse DNS notation)", max_length=128, unique=True
            ),
        ),
    ]
