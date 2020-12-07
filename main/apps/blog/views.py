# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import AboutMe, Article, Comment

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ArticleList
# Create your views here.

def main(request):
    blog_articles_list = Article.objects.order_by('-pub_date')
    return render(request, 'blog/main.html', {'list': blog_articles_list})


def article(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
        b = Comment.objects.filter(article=a.id)
    except:
        raise Http404("Статья не найдена") 
    
    #latest_comments_list = a.comment_set.order_by('-id')[:10]

    return render (request, 'blog/article.html', {'article': a, 'comment': b})

def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404("Статья не найдена")

    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])
    return HttpResponseRedirect(reverse('article', args=(a.id,)))

class ArticleListView(APIView):
    def get(self, request):
        article = Article.objects.order_by('-pub_date')
        serializer = ArticleList(article, many=True)
        return Response(serializer.data)