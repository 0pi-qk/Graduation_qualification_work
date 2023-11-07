from django.db import models

import Core.models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=2500, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()
    image = models.CharField(max_length=256)


class StarProduct(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Core.models.Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    evaluation = models.IntegerField()


class OnlineOrder(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Core.models.Account, on_delete=models.CASCADE)
    PAY = (
        ('online', 'online'),
        ('offline', 'offline'),
    )
    payment_metod = models.CharField(max_length=7, choices=PAY)
    RECEIVING = (
        ('delivery', 'delivery'),
        ('self-delivery', 'self-delivery'),
    )
    metod_of_receipt = models.CharField(max_length=13, choices=RECEIVING)
    date_of_order = models.DateField()
    order_time = models.TimeField()
    amount = models.DecimalField(max_digits=9, decimal_places=2)


class OrderProduct(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(OnlineOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Core.models.Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
