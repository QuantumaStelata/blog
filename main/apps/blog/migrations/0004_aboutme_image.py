# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-18 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201018_0404'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]