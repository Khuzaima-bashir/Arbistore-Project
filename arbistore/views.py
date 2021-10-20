from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenViewBase

from arbistore.models import Product, User, Category
from arbistore.serializers import CategorySerializer, ProductsSerializer, RegisterSerializer, TokenObtainPairSerializer\
    , UserTokenVerifySerializer


class ProductList(APIView, LimitOffsetPagination):

    def get(self, request):
        products = Product.objects.all()
        results = self.paginate_queryset(products, request, view=self)
        serialized_products = ProductsSerializer(results, many=True)
        return self.get_paginated_response(serialized_products.data)


class Categories(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class ProductFetch(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer


class TokenObtainPairView(TokenViewBase):
    serializer_class = TokenObtainPairSerializer


class TokenVerifyView(TokenViewBase):
    serializer_class = UserTokenVerifySerializer


class CategoryProductFetch(APIView, LimitOffsetPagination):

    def get(self, request, pk):
        products = Product.objects.filter(category_name=pk)
        results = self.paginate_queryset(products, request, view=self)
        serialized_products = ProductsSerializer(results, many=True)
        return self.get_paginated_response(serialized_products.data)


class SubCategoryProductFetch(APIView, LimitOffsetPagination):

    def get(self, request, pk):
        products = Product.objects.filter(sub_categories=pk)
        results = self.paginate_queryset(products, request, view=self)
        serialized_products = ProductsSerializer(results, many=True)
        return self.get_paginated_response(serialized_products.data)
