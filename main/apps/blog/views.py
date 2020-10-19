# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .models import AboutMe, Article, Comment
# Create your views here.

def main(request):
    #latest_articles_list = Article.objects.order_by('-pub_date')
    return render(request, 'blog/main.html')#, {'articles_list': latest_articles_list})

def about_me(request):
    about_me_text = AboutMe.objects.order_by('about_me')
    return render(request, 'blog/about_me.html', {'about_me_text': about_me_text})

def my_blog(request):
    blog_articles_list = Article.objects.order_by('-pub_date')
    return render(request, 'blog/my_blog.html', {'list': blog_articles_list})

def article(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404("Статья не найдена")

    return render (request, 'blog/article.html', {'article': a})