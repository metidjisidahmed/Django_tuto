from rest_framework import generics
from .models import Products
from .serializers import ProductsSerializer

# generics are so useful to do the classic GET/POST/PATCH/DELETE t requests with its defined validators for the serilizer_class

class RetrieveProductGeneric(generics.RetrieveAPIView):
    # the query set is the set of objects that the query woul be applied List[Products]
    queryset = Products.objects.all()
    # Its The serializer class of the queryset objects
    serializer_class = ProductsSerializer
    # /search_produtcs/1 : will search the product where product.pk = 1 ( pk is a default created field representing the primary key )
    # lookup_field = "pk"


class RetrieveListProductsGeneric(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class CreateProductGeneric(generics.CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


generic_search_product_route = RetrieveProductGeneric.as_view()
generic_create_product_route = CreateProductGeneric.as_view()
generic_get_all_products_route = RetrieveListProductsGeneric.as_view()