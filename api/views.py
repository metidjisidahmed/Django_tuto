import json

from django.http import JsonResponse


# Create your views here.
def main_route(request, *args, **kwargs):
    response = dict()
    response['text'] = "MY FIRST DJANGO RESPONSE"
    response['query'] = request.GET
    response['body'] = json.loads(request.body)
    response['headers'] = dict(request.headers)
    return JsonResponse({"success": True, "data": response, "error": None})
