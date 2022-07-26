import json

from django.http import JsonResponse
from .models import Products


# Create your views here.
def main_route(request, *args, **kwargs):
    print("REQUEST BODY =", request.body)
    # get random product
    random_product = Products.objects.all().order_by("?").first()
    response = dict()
    response['text'] = "MY FIRST DJANGO RESPONSE"
    response['query'] = request.GET
    response['body'] = json.loads(request.body)
    response['headers'] = dict(request.headers)
    response['product']= random_product.name + " id= " + str(random_product.id)
    return JsonResponse({"success": True, "data": response, "error": None})


def create_product_route(request, *args, **kwargs):
    print("REQUEST BODY =", request.body)
    product_params = json.loads(request.body)
    created_product = Products.objects.create(name=product_params['name'], content=product_params['content'],
                                              price=product_params['price'])
    return JsonResponse({"success": True, "data": created_product.id, "error": None})
