import json

from django.http import JsonResponse
# our product schema
#api_view is used to specify the type of allowed methods ( get/post ...)
from rest_framework.decorators import api_view
#response is useful to create a nice doc for our api
from rest_framework.response import Response

from .models import Products
# modelèto_dict is useful to convert our model to dict so we can send it as a response through JsonResponse object
from django.forms.models import model_to_dict
# Serilizer is a better alternative for mode_to_dict because he usues a serializable instance to map all the fields including the @property ones
from .serializers import ProductsSerializer

# Create your views here.
@api_view(["GET"])
def main_route(request, *args, **kwargs):
    print("REQUEST BODY =", request.body)
    # get random product
    response = dict()
    response['text'] = "MY FIRST DJANGO RESPONSE"
    response['query'] = request.GET
    response['body'] = json.loads(request.body)
    response['headers'] = dict(request.headers)

    return Response({"success": True, "data": response, "error": None})

@api_view(["GET"])
def get_product_route(request, *args, **kwargs):
    print("REQUEST BODY =", request.body)
    # get random product
    product_instance = Products.objects.all().order_by("?").first()
    product_serializable = ProductsSerializer(product_instance)
    response = dict()
    response['product'] = product_serializable.data
    return Response({"success": True, "data": response, "error": None})

@api_view(["POST"])
def create_product_route(request, *args, **kwargs):
    print("REQUEST BODY =", request.body)
    product_params = json.loads(request.body)
    product_instance = Products.objects.all().order_by("?").first()
    created_product = Products.objects.create(name=product_params['name'], content=product_params['content'],
                                              price=product_params['price'])
    product_serializable = ProductsSerializer(created_product)

    return Response({"success": True, "data": model_to_dict(product_serializable.data, fields=["id", "name"]), "error": None})

# In this endpoint im gonna apply a validator like JOI where it will verify if my body params matches my Models
# my model has only 'name' field as a required field
# get discount price has to do the calculation only if our body has discount attribute
@api_view(["POST"])
def create_product_by_name_route(request, *args, **kwargs):
    print("REQUEST BODY =", request.body)
    product_params=dict()
    if request.body:
        product_params = json.loads(request.body)

    productSerializable= ProductsSerializer(data=product_params)
    if productSerializable.is_valid(raise_exception=True):
        result_product = productSerializable.data
        # created_product = Products.objects.create(name=product_params['name'], content=product_params['content'],
        #                                           price=product_params['price'])
        return Response({"success": True, "data": result_product, "error": None})
