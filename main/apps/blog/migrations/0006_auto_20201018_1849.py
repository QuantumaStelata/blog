# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-18 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_publicate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutme',
            name='image',
        ),
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]
