# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 05:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0003_record_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='profilePic',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]
