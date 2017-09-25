# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 11:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0006_auto_20170925_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='address',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='afternoonTimeSlot',
            field=models.TimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='clinicName',
            field=models.CharField(default=None, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='eveningTimeSlot',
            field=models.TimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='morningTimeSlot',
            field=models.TimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='profilePic',
            field=models.ImageField(null=True, upload_to='profile_pics', verbose_name='Profile Picture'),
        ),
        migrations.AlterField(
            model_name='record',
            name='services',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='specialization',
            field=models.CharField(default=None, max_length=256, null=True),
        ),
    ]