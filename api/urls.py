from django.urls import path

from api import views

urlpatterns = [
    path('get_random_product/', views.main_route),
    path('create_product/', views.create_product_route)
]
