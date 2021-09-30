from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from arbistore.models import Product, User, Category
from arbistore.serializers import CategorySerializer, ProductsSerializer, RegisterSerializer


class ProductList(ListAPIView):

    def get(self, request, format=None):
        products = Product.objects.all()
        serialize = ProductsSerializer(products, many=True)
        return Response(serialize.data)


class Categories(APIView):

    def get(self, request, format=None):
        categories = Category.objects.all()
        serialize = CategorySerializer(categories, many=True)
        return Response(serialize.data)


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class ProductFetch(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
