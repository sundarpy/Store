# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 13:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appstore', '0011_auto_20160701_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='app_apk',
        ),
        migrations.RemoveField(
            model_name='application',
            name='app_icon',
        ),
        migrations.RemoveField(
            model_name='application',
            name='states',
        ),
        migrations.RemoveField(
            model_name='applicationimage',
            name='image_file',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='email',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='privacy_policy',
        ),
        migrations.RemoveField(
            model_name='publisher',
            name='website',
        ),
    ]
