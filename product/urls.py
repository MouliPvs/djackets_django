
from django.urls import path, include

from product import views

urlpatterns = [
    # Latest-Products Details
    path('latest-products', views.LatestProductsList.as_view()),

    # Single Product Details
    path('products/<slug:category_slug>/<slug:product_slug>', views.ProductDetails.as_view()),
]
 