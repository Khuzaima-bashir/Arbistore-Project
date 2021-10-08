import jwt
from django.contrib.auth.models import update_last_login
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import CharField, EmailField, ModelSerializer, StringRelatedField
from rest_framework_simplejwt.serializers import TokenObtainSerializer, TokenVerifySerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from rest_framework_simplejwt.tokens import RefreshToken

from arbistore.models import Category, Product, SubCategories, User, ProductColor, ProductImage, ProductSizeStock
from ArbistoreProject.settings import SECRET_KEY


class RegisterSerializer(ModelSerializer):
    email = EmailField(required=True, )
    password = CharField(write_only=True, required=True, validators=[validate_password, ])

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'full_name', 'address')

    def create(self, validated_data):
        user = User.objects.create(
            **validated_data
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class TokenObtainPairSerializer(TokenObtainSerializer):

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        my_user = User.objects.filter(pk=self.user.id).first()
        if my_user:
            data['user'] = UserSerializer(my_user).data

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class UserTokenVerifySerializer(TokenVerifySerializer):

    def validate(self, attrs):
        token = attrs['token']
        if api_settings.BLACKLIST_AFTER_ROTATION:
            jti = token.get(api_settings.JTI_CLAIM)
            if BlacklistedToken.objects.filter(token__jti=jti).exists():
                raise ValidationError("Token is blacklisted")

        else:
            valid_data = jwt.decode(token, SECRET_KEY,
                                    algorithms=["HS256"])
            my_user = User.objects.filter(pk=valid_data['user_id']).first()
            user_data = UserSerializer(my_user).data

        return {"user_data": user_data}


class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = SubCategories
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    sub_categories = StringRelatedField(many=True)

    class Meta:
        model = Category
        fields = ('name', 'sub_categories')


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("image",)


class ProductSizeStockSerializer(ModelSerializer):
    class Meta:
        model = ProductSizeStock
        fields = ("size", "stock")


class ProductColorSerializer(ModelSerializer):
    product_size_stock = ProductSizeStockSerializer(many=True)
    product_color_image = ProductImageSerializer(many=True)

    class Meta:
        model = ProductColor
        fields = ("color", "product_size_stock", "product_color_image")


class ProductsSerializer(ModelSerializer):
    product_detail = ProductColorSerializer(many=True)
    category_name = ProductCategorySerializer()
    sub_categories = StringRelatedField(many=True)
    brand = StringRelatedField()

    class Meta:
        model = Product
        fields = ("id", "name", "gender", "price", "product_detail", "category_name",
                  "sub_categories", "brand", "full_description")
