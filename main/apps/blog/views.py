# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import AboutMe, Article, Comment
# Create your views here.

def main(request):
    #latest_articles_list = Article.objects.order_by('-pub_date')
    return render(request, 'blog/main.html')#, {'articles_list': latest_articles_list})

def about_me(request):
    about_me_text = AboutMe.objects.order_by('about_me')
    return render(request, 'blog/about_me.html', {'about_me_text': about_me_text})