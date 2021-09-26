from django.http import Http404
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
        """Returns First 4 Latest Product Objects From DataBase In Json"""
        products = Product.objects.all()[0 : 4]

        #converts products into serializer, many=True because we have more than one object
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)

class ProductDetails(APIView):
    """For Displaying The Single Product Details Clicked By User"""
    def get_object(self, category_slug, product_slug):
        "Returns The Product Object If product doesn't exists returns Http404 error"
        # check if object exists
        try:
            # filters every product in category  & get product url from that
            return Product.objects.filter(category_slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, category_slug, product_slug, format=None):
        """Returns Single Product Object Data In Json"""
        product = self.get_object(category_slug, product_slug)
        # converts products into serializer,
        serializer = ProductSerializer(product)
        return Response(serializer.data)