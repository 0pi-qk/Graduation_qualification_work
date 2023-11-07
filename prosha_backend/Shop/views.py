from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Shop.models import Product, StarProduct, OnlineOrder, OrderProduct, Cart
from Shop.serializers import ProductSerializer, StarProductSerializer, \
    OnlineOrderSerializer, OrderProductSerializer, CartSerializer

from django.core.files.storage import default_storage

@csrf_exempt
def productApi(request, section=None):
    if request.method == 'GET':
        if section == 'all':
            product = Product.objects.all()
        else:
            product = Product.objects.all().filter(id=section)
        product_serializer = ProductSerializer(product, many=True)
        return JsonResponse(product_serializer.data, safe=False)
    elif request.method == 'POST':
        product_data = JSONParser().parse(request)
        product_serializer = ProductSerializer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse(product_serializer.data, safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        product_data = JSONParser().parse(request)
        product = Product.objects.get(id=product_data['id'])
        product_serializer = ProductSerializer(product, data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse(product_serializer.data, safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        product = Product.objects.get(id=section)
        product.delete()
        return JsonResponse(section, safe=False)


@csrf_exempt
def starproductApi(request, section=None):
    if request.method == 'GET':
        starproduct = StarProduct.objects.all().filter(product=section)
        starproduct_serializer = StarProductSerializer(starproduct, many=True)
        return JsonResponse(starproduct_serializer.data, safe=False)
    elif request.method == 'POST':
        starproduct_data = JSONParser().parse(request)
        starproduct_serializer = StarProductSerializer(data=starproduct_data)
        if starproduct_serializer.is_valid():
            starproduct_serializer.save()
            return JsonResponse(starproduct_serializer.data, safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        starproduct_data = JSONParser().parse(request)
        starproduct = StarProduct.objects.get(id=starproduct_data['id'])
        starproduct_serializer = StarProductSerializer(starproduct, data=starproduct_data)
        if starproduct_serializer.is_valid():
            starproduct_serializer.save()
            return JsonResponse(starproduct_serializer.data, safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        starproduct = StarProduct.objects.get(id=section)
        starproduct.delete()
        return JsonResponse(section, safe=False)


@csrf_exempt
def onlineorderApi(request, section=None):
    if request.method == 'GET':
        onlineorder = OnlineOrder.objects.all().filter(user=section)
        onlineorder_serializer = OnlineOrderSerializer(onlineorder, many=True)
        return JsonResponse(onlineorder_serializer.data, safe=False)
    elif request.method == 'POST':
        onlineorder_data = JSONParser().parse(request)
        onlineorder_serializer = OnlineOrderSerializer(data=onlineorder_data)
        if onlineorder_serializer.is_valid():
            onlineorder_serializer.save()
            return JsonResponse(onlineorder_serializer.data, safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        onlineorder_data = JSONParser().parse(request)
        onlineorder = OnlineOrder.objects.get(id=onlineorder_data['id'])
        onlineorder_serializer = OnlineOrderSerializer(onlineorder, data=onlineorder_data)
        if onlineorder_serializer.is_valid():
            onlineorder_serializer.save()
            return JsonResponse(onlineorder_serializer.data, safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        onlineorder = OnlineOrder.objects.get(id=section)
        onlineorder.delete()
        return JsonResponse(section, safe=False)


@csrf_exempt
def orderproductApi(request, section=None):
    if request.method == 'GET':
        orderproduct = OrderProduct.objects.all().filter(user=section)
        orderproduct_serializer = OrderProductSerializer(orderproduct, many=True)
        return JsonResponse(orderproduct_serializer.data, safe=False)
    elif request.method == 'POST':
        orderproduct_data = JSONParser().parse(request)
        orderproduct_serializer = OrderProductSerializer(data=orderproduct_data)
        if orderproduct_serializer.is_valid():
            orderproduct_serializer.save()
            return JsonResponse(orderproduct_serializer.data, safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        orderproduct_data = JSONParser().parse(request)
        orderproduct = OrderProduct.objects.get(id=orderproduct_data['id'])
        orderproduct_serializer = OrderProductSerializer(orderproduct, data=orderproduct_data)
        if orderproduct_serializer.is_valid():
            orderproduct_serializer.save()
            return JsonResponse(orderproduct_serializer.data, safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        orderproduct = OrderProduct.objects.get(id=section)
        orderproduct.delete()
        return JsonResponse(section, safe=False)


@csrf_exempt
def cartApi(request, section=None):
    if request.method == 'GET':
        cart = Cart.objects.all().filter(user=section)
        cart_serializer = CartSerializer(cart, many=True)
        return JsonResponse(cart_serializer.data, safe=False)
    elif request.method == 'POST':
        cart_data = JSONParser().parse(request)
        cart_serializer = CartSerializer(data=cart_data)
        if cart_serializer.is_valid():
            cart_serializer.save()
            return JsonResponse(cart_serializer.data, safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        cart_data = JSONParser().parse(request)
        cart = Cart.objects.get(id=cart_data['id'])
        cart_serializer = CartSerializer(cart, data=cart_data)
        if cart_serializer.is_valid():
            cart_serializer.save()
            return JsonResponse(cart_serializer.data, safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        cart = Cart.objects.get(id=section)
        cart.delete()
        return JsonResponse(section, safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
