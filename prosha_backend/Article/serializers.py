from rest_framework import serializers
from Article.models import Article, StarArticle


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'user', 'title', 'description', 'date_of_publication', 'image')


class StarArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarArticle
        fields = ('id', 'user', 'article', 'evaluation')
