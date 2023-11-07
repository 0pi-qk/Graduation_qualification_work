from rest_framework import serializers
from News.models import News, StarNews


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'user', 'title', 'description', 'date_of_publication', 'image')


class StarNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarNews
        fields = ('id', 'user', 'news', 'evaluation')
