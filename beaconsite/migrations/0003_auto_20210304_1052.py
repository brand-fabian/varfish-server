# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-04 10:52
from __future__ import unicode_literals

from django.db import migrations
import encrypted_model_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ("beaconsite", "0002_auto_20210304_0716"),
    ]

    operations = [
        migrations.AlterField(
            model_name="site",
            name="private_key",
            field=encrypted_model_fields.fields.EncryptedTextField(
                blank=True, help_text="(Private) key for (a)symmetric encryption.", null=True
            ),
        ),
    ]
