# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime

from django.utils import timezone

# Create your models here.

class Article(models.Model):
    article_title = models.CharField('Название статьи', max_length = 200)
    article_text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации статьи')

    def __str__(self):
        return self.article_title

    def was(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    author_name = models.CharField('Имя автора', max_length = 100)
    comment_text = models.CharField('Текст статьи', max_length = 500)

    def __str__(self):
        return self.author_name


    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'