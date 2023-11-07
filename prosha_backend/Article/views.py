from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Article.models import Article, StarArticle
from Article.serializers import ArticleSerializer, StarArticleSerializer

from django.core.files.storage import default_storage

@csrf_exempt
def articleApi(request, section=None):
    if request.method == 'GET':
        if section == 'all':
            article = Article.objects.all()
        else:
            article = Article.objects.all().filter(id=section)
        article_serializer = ArticleSerializer(article, many=True)
        return JsonResponse(article_serializer.data, safe=False)
    elif request.method == 'POST':
        article_data = JSONParser().parse(request)
        article_serializer = ArticleSerializer(data=article_data)
        if article_serializer.is_valid():
            article_serializer.save()
            return JsonResponse(article_serializer.data, safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        article_data = JSONParser().parse(request)
        article = Article.objects.get(id=article_data['id'])
        article_serializer = ArticleSerializer(article, data=article_data)
        if article_serializer.is_valid():
            article_serializer.save()
            return JsonResponse(article_serializer.data, safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        article = Article.objects.get(id=section)
        article.delete()
        return JsonResponse(section, safe=False)


@csrf_exempt
def stararticleApi(request, section=None):
    if request.method == 'GET':
        stararticle = StarArticle.objects.all().filter(article=section)
        stararticle_serializer = StarArticleSerializer(stararticle, many=True)
        return JsonResponse(stararticle_serializer.data, safe=False)
    elif request.method == 'POST':
        stararticle_data = JSONParser().parse(request)
        stararticle_serializer = StarArticleSerializer(data=stararticle_data)
        if stararticle_serializer.is_valid():
            stararticle_serializer.save()
            return JsonResponse(stararticle_serializer.data, safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        stararticle_data = JSONParser().parse(request)
        stararticle = StarArticle.objects.get(id=stararticle_data['id'])
        stararticle_serializer = StarArticleSerializer(stararticle, data=stararticle_data)
        if stararticle_serializer.is_valid():
            stararticle_serializer.save()
            return JsonResponse(stararticle_serializer.data, safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        stararticle = StarArticle.objects.get(id=section)
        stararticle.delete()
        return JsonResponse(section, safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
