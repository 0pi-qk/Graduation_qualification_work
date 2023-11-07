from rest_framework import serializers
from Core.models import Account, Address, Bird, Exchange


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'name', 'last_name', 'email', 'login', 'password', 'role')


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'user', 'country', 'city', 'street', 'flat')


class BirdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bird
        fields = ('id', 'user', 'number', 'name', 'date_of_birth', 'parent1', 'parent2', 'gender')


class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = ('id', 'user_former', 'bird', 'code', 'status')
