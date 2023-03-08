from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=64)

class Product(models.Model):
    name = models.CharField(max_length=32)
    unit = models.CharField(max_length=32)
    price = models.FloatField()
    supplierid = models.PositiveIntegerField()
    categoryid = models.PositiveIntegerField()

class OrderDetail(models.Model):
    no = models.PositiveIntegerField()
    date = models.DateField()
    pid = models.PositiveIntegerField()
    qty = models.PositiveIntegerField()
    cid = models.CharField(max_length=4)
    channel = models.PositiveIntegerField()

