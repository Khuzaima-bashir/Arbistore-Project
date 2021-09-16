from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from arbistore.models import Products, User, Category, SubCategory
from arbistore.serializers import RegisterSerializer, ProductsSerializer


class ProductList(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        products = Products.objects.all()
        serialize = ProductsSerializer(products, many=True)
        return Response(serialize.data)


class Categories(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        categories = [category.name for category in Category.objects.all()]
        return Response(categories)


class SubCategories(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        sub_categories = [sub_category.name for sub_category in SubCategory.objects.all()]
        return Response(sub_categories)


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class ProductFetch(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        product = Products.objects.get(pk=pk)
        serialized_product = ProductsSerializer(product)
        return Response(serialized_product.data)
