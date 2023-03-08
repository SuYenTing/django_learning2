from django.contrib import admin
from order.models import UserInfo, Product, OrderDetail

admin.site.register(UserInfo)
admin.site.register(Product)
admin.site.register(OrderDetail)