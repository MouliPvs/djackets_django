from django.contrib import admin

from .models import Category, Product

# Register your models here.

#Registering "Category" Model To Access In Admin Panel
admin.site.register(Category)

#Registering "Product" Model To Access In Admin Panel
admin.site.register(Product)

