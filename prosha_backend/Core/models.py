from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class Account(AbstractBaseUser, PermissionsMixin):
    REQUIRED_FIELDS = ['name']
    USERNAME_FIELD = 'email'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.CharField(max_length=319, null=True, unique=True)
    login = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    USER_ROLE = (
        ('User', 'User'),
        ('Breeder', 'Breeder'),
        ('Manager', 'Manager'),
        ('Admin', 'Admin'),
    )
    role = models.CharField(max_length=7, choices=USER_ROLE)


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    country = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=128)
    flat = models.CharField(max_length=32, null=True)


class Bird(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    number = models.CharField(max_length=64, null=True)
    name = models.CharField(max_length=256, null=True)
    date_of_birth = models.DateField(null=True)
    parent1 = models.CharField(max_length=64, null=True)
    parent2 = models.CharField(max_length=64, null=True)
    GENDER_BIRD = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('None', 'None'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_BIRD)


class Exchange(models.Model):
    id = models.AutoField(primary_key=True)
    user_former = models.ForeignKey(Account, on_delete=models.CASCADE)
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)
    code = models.CharField(max_length=128)
    STATUS_EXCHANGE = (
        ('Active', 'Active'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    status = models.CharField(max_length=9, choices=STATUS_EXCHANGE)
