from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from arbistore.models import Product, User, Category, SubCategory
from arbistore.serializers import CategorySerializer, ProductsSerializer, RegisterSerializer, SubCategorySerializer


class ProductList(APIView):

    def post(self, request, format=None):
        products = Product.objects.all()
        serialize = ProductsSerializer(products, many=True)
        return Response(serialize.data)

    def get(self, request, format=None):
        products = Product.objects.all()
        serialize = ProductsSerializer(products, many=True)
        return Response(serialize.data)


class Categories(APIView):

    def post(self, request, format=None):
        categories = Category.objects.all()
        serialize = CategorySerializer(categories, many=True)
        return Response(serialize.data)

    def get(self, request, format=None):
        categories = Category.objects.all()
        serialize = CategorySerializer(categories, many=True)
        return Response(serialize.data)


class SubCategories(APIView):

    def post(self, request, format=None):
        sub_categories = SubCategory.objects.all()
        serialize = SubCategorySerializer(sub_categories, many=True)
        return Response(serialize.data)

    def get(self, request, format=None):
        sub_categories = SubCategory.objects.all()
        serialize = SubCategorySerializer(sub_categories, many=True)
        return Response(serialize.data)


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class ProductFetch(RetrieveAPIView):

    def post(self, request, pk):
        product = Product.objects.get(pk=pk)
        serialized_product = ProductsSerializer(product)
        return Response(serialized_product.data)
