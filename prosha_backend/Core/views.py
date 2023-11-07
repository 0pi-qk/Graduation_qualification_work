from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Core.models import Account, Address, Bird, Exchange
from Core.serializers import AccountSerializer, AddressSerializer, BirdSerializer, ExchangeSerializer


@csrf_exempt
def accountApi(request, section=None):
    if request.method == 'GET':
        account = Account.objects.all().filter(id=section)
        account_serializer = AccountSerializer(account, many=True)
        return JsonResponse(account_serializer.data, safe=False)
    elif request.method == 'POST':
        account_data = JSONParser().parse(request)
        account_serializer = AccountSerializer(data=account_data)
        if account_serializer.is_valid():
            account_serializer.save()
            return JsonResponse(account_serializer.data, safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        account_data = JSONParser().parse(request)
        account = Account.objects.get(id=account_data['id'])
        account_serializer = AccountSerializer(account, data=account_data)
        if account_serializer.is_valid():
            account_serializer.save()
            return JsonResponse(account_serializer.data, safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        account = Account.objects.get(id=section)
        account.delete()
        return JsonResponse(section, safe=False)


@csrf_exempt
def addressApi(request, section=None):
    if request.method == 'GET':
        address = Address.objects.all().filter(user=section)
        address_serializer = AddressSerializer(address, many=True)
        return JsonResponse(address_serializer.data, safe=False)
    elif request.method == 'POST':
        address_data = JSONParser().parse(request)
        address_serializer = AddressSerializer(data=address_data)
        if address_serializer.is_valid():
            address_serializer.save()
            return JsonResponse(address_serializer.data, safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        address_data = JSONParser().parse(request)
        address = Address.objects.get(id=address_data['id'])
        address_serializer = AddressSerializer(address, data=address_data)
        if address_serializer.is_valid():
            address_serializer.save()
            return JsonResponse(address_serializer.data, safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        address = Address.objects.get(id=section)
        address.delete()
        return JsonResponse(section, safe=False)


@csrf_exempt
def birdApi(request, section=None, user=None):
    if request.method == 'GET':
        if section == 'tree':
            bird = Bird.objects.all()
        elif section == 'user':
            bird = Bird.objects.all().filter(user=user)
        else:
            bird = Bird.objects.all().filter(id=section)
        bird_serializer = BirdSerializer(bird, many=True)
        return JsonResponse(bird_serializer.data, safe=False)
    elif request.method == 'POST':
        bird_data = JSONParser().parse(request)
        bird_serializer = BirdSerializer(data=bird_data)
        if bird_serializer.is_valid():
            bird_serializer.save()
            return JsonResponse(bird_serializer.data, safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        bird_data = JSONParser().parse(request)
        bird = Bird.objects.get(id=bird_data['id'])
        bird_serializer = BirdSerializer(bird, data=bird_data)
        if bird_serializer.is_valid():
            bird_serializer.save()
            return JsonResponse(bird_serializer.data, safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        bird = Bird.objects.get(id=section)
        bird.delete()
        return JsonResponse(section, safe=False)


@csrf_exempt
@csrf_exempt
def exchangeApi(request, section=None):
    if request.method == 'GET':
        exchange = Exchange.objects.all()
        exchange_serializer = ExchangeSerializer(exchange, many=True)
        return JsonResponse(exchange_serializer.data, safe=False)
    elif request.method == 'POST':
        exchange_data = JSONParser().parse(request)
        exchange_serializer = ExchangeSerializer(data=exchange_data)
        if exchange_serializer.is_valid():
            exchange_serializer.save()
            return JsonResponse(exchange_serializer.data, safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        exchange_data = JSONParser().parse(request)
        exchange = Exchange.objects.get(id=exchange_data['id'])
        exchange_serializer = ExchangeSerializer(exchange, data=exchange_data)
        if exchange_serializer.is_valid():
            exchange_serializer.save()
            return JsonResponse(exchange_serializer.data, safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        exchange = Exchange.objects.get(id=section)
        exchange.delete()
        return JsonResponse(section, safe=False)

