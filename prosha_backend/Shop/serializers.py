from rest_framework import serializers
from Shop.models import Product, StarProduct, OnlineOrder, OrderProduct, Cart


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'quantity', 'image')


class StarProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarProduct
        fields = ('id', 'user', 'product', 'evaluation')


class OnlineOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineOrder
        fields = ('id', 'user', 'payment_metod', 'metod_of_receipt', 'date_of_order', 'order_time', 'amount')


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ('id', 'order', 'product', 'quantity')


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'user', 'product', 'quantity')
