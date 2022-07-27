import json

from django.http import JsonResponse
# our product schema
from .models import Products
# modelèto_dict is useful to convert our model to dict so we can send it as a response through JsonResponse object
from django.forms.models import model_to_dict

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

    response['product']= model_to_dict(random_product)
    return JsonResponse({"success": True, "data": response, "error": None})


def create_product_route(request, *args, **kwargs):
    print("REQUEST BODY =", request.body)
    product_params = json.loads(request.body)
    created_product = Products.objects.create(name=product_params['name'], content=product_params['content'],
                                              price=product_params['price'])
    return JsonResponse({"success": True, "data": model_to_dict(created_product , fields=["id" , "name"]), "error": None})
