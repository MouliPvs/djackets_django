from django.contrib import admin

from .models import Category, Product

# Register your models here.

#Registering "Category" Model
admin.site.register(Category)

#Registering "Product" Model
admin.site.register(Product)

