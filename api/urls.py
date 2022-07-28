from django.urls import path

from api import views

urlpatterns = [
    path('get_random_product', views.get_product_route),
    path('test', views.main_route),
    path('create_product', views.create_product_route),
    path('create_product_by_name', views.create_product_by_name_route)
]
