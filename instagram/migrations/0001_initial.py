# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-15 20:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='profile_pics')),
                ('bio', models.CharField(blank=True, max_length=200, null=True)),
                ('followers', models.ManyToManyField(blank=True, related_name='profile_followers', to='instagram.Profile')),
                ('following', models.ManyToManyField(blank=True, related_name='following_profile', to='instagram.Profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
