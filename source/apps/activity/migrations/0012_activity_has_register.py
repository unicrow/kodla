# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-03-15 08:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0011_activity_has_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='has_register',
            field=models.BooleanField(default=False, verbose_name='Register'),
        ),
    ]