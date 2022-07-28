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
    response = dict()
    response['product'] = ProductsSerializer(product_instance).data
    return Response({"success": True, "data": response, "error": None})

@api_view(["POST"])
def create_product_route(request, *args, **kwargs):
    print("REQUEST BODY =", request.body)
    product_params = json.loads(request.body)
    created_product = Products.objects.create(name=product_params['name'], content=product_params['content'],
                                              price=product_params['price'])
    return Response({"success": True, "data": model_to_dict(created_product, fields=["id", "name"]), "error": None})
