# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Article, Comment
# Create your views here.

def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')
    return render(request, 'blog/list.html', {'articles_list': latest_articles_list})