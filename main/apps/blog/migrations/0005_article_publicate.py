# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-18 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_aboutme_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='publicate',
            field=models.BooleanField(default=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u0442\u044c?'),
        ),
    ]
