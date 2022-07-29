from django.urls import path

from api import views
from api.generics import generic_search_product_route, generic_create_product_route, generic_get_all_products_route

urlpatterns = [
    path('get_random_product', views.get_product_route),
    path('test', views.main_route),
    path('create_product', views.create_product_route),
    path('create_product_by_name', views.create_product_by_name_route),
    path('generics/search_product/<int:pk>', generic_search_product_route),
    path('generics/search_product/all', generic_get_all_products_route),
    path('generics/create_product', generic_create_product_route),
]
