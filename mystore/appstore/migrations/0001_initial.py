# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 09:03
from __future__ import unicode_literals

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(blank=True, max_length=100, null=True)),
                ('app_slug', autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='app_name')),
                ('app_description', models.TextField(blank=True, null=True)),
                ('app_rating', models.CharField(blank=True, max_length=10, null=True)),
                ('app_pubdate', models.CharField(blank=True, max_length=25, null=True)),
                ('app_version', models.CharField(blank=True, max_length=10, null=True)),
                ('app_size', models.CharField(blank=True, max_length=10, null=True)),
                ('app_type', models.CharField(blank=True, choices=[('A', 'Application'), ('G', 'Game'), ('O', 'Other')], max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(blank=True, max_length=200, null=True)),
                ('app_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appstore.Application')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, null=True)),
                ('category_slug', autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='category_name')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_name', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('collection_items', models.ManyToManyField(to='appstore.Application')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='name')),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='app_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appstore.Category'),
        ),
        migrations.AddField(
            model_name='application',
            name='app_publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appstore.Publisher'),
        ),
    ]
