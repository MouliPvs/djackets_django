"""Serializers get information from database & turn them into json & we use them in front end"""
from django.db.models import fields
from rest_framework import serializers

#.models because models.py & seriliazers.py are same folder
from .models import Category, Product

#Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail",
        )
class CategorySerializer(serializers.ModelSerializer):
    # Gets All The Products Under This Category
    products = ProductSerializer(many= True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        )