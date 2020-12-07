from .models import Article
from rest_framework import serializers

class ArticleList(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('article_title', 'article_text', )