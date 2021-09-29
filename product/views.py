from django.http import Http404
from django.shortcuts import render
from rest_framework import serializers

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
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
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    # Gets Request When User Hits The Url
    # Gets Input From /product/urls.py : path('products/<slug:category_slug>/<slug:product_slug>', views.ProductDetails.as_view())
    def get(self, request, category_slug, product_slug, format=None):
        """Returns Single Product Details Data In Json"""
        product = self.get_object(category_slug, product_slug)
        # converts products into serializer,
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class CategoryDetail(APIView):
    """For Displaying Category Details Clicked By User"""
    def get_object(self, category_slug):
        "Returns The Category Object If category doesn't exists returns Http404 error"
        # check if object exists
        try:
            # Gets The Category Slug
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    # Gets Request When User Hits The Url
    # Gets Input From /product/urls.py : path('products/<slug:category_slug>/<slug:product_slug>', views.ProductDetails.as_view())
    def get(self, request, category_slug, format=None):
        """Returns Single Category Details Data In Json"""
        category = self.get_object(category_slug)
        # converts products into serializer,
        serializer = CategorySerializer(category)
        return Response(serializer.data)
