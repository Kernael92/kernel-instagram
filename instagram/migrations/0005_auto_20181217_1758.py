# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-17 14:58
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_auto_20181217_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='images'),
        ),
    ]