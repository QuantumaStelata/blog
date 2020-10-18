# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import AboutMe, Article, Comment
# Register your models here.
admin.site.register(Comment)
admin.site.register(AboutMe)
admin.site.register(Article)
