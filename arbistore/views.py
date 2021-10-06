from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenViewBase

from arbistore.models import Product, User, Category
from arbistore.serializers import CategorySerializer, ProductsSerializer, RegisterSerializer, TokenObtainPairSerializer


class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer


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
