from django.shortcuts import render
from rest_framework import serializers

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer
# Create your views here.

class LatestProductsList(APIView):
    """Get The Latest Products On The Front Page"""
    def get(self, request, format=None):
        #Gets First 4 Latest Product Objects From DataBase
        products = Product.objects.all()[0 : 4]

        #converts products into serializer, many=True because we have more than one object
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)