from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from News.models import News, StarNews
from News.serializers import NewsSerializer, StarNewsSerializer

from django.core.files.storage import default_storage

@csrf_exempt
def newsApi(request, section=None):
    if request.method == 'GET':
        if section == 'all':
            news = News.objects.all()
        else:
            news = News.objects.all().filter(id=section)
        news_serializer = NewsSerializer(news, many=True)
        return JsonResponse(news_serializer.data, safe=False)
    elif request.method == 'POST':
        news_data = JSONParser().parse(request)
        news_serializer = NewsSerializer(data=news_data)
        if news_serializer.is_valid():
            news_serializer.save()
            return JsonResponse(news_serializer.data, safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        news_data = JSONParser().parse(request)
        news = News.objects.get(id=news_data['id'])
        news_serializer = NewsSerializer(news, data=news_data)
        if news_serializer.is_valid():
            news_serializer.save()
            return JsonResponse(news_serializer.data, safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        news = News.objects.get(id=section)
        news.delete()
        return JsonResponse(section, safe=False)


@csrf_exempt
def starnewsApi(request, section=None):
    if request.method == 'GET':
        starnews = StarNews.objects.all().filter(news=section)
        starnews_serializer = StarNewsSerializer(starnews, many=True)
        return JsonResponse(starnews_serializer.data, safe=False)
    elif request.method == 'POST':
        starnews_data = JSONParser().parse(request)
        starnews_serializer = StarNewsSerializer(data=starnews_data)
        if starnews_serializer.is_valid():
            starnews_serializer.save()
            return JsonResponse(starnews_serializer.data, safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        starnews_data = JSONParser().parse(request)
        starnews = StarNews.objects.get(id=starnews_data['id'])
        starnews_serializer = StarNewsSerializer(starnews, data=starnews_data)
        if starnews_serializer.is_valid():
            starnews_serializer.save()
            return JsonResponse(starnews_serializer.data, safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        starnews = StarNews.objects.get(id=section)
        starnews.delete()
        return JsonResponse(section, safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
