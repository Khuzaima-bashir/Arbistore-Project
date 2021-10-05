from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import CharField, EmailField, ModelSerializer, StringRelatedField

from arbistore.models import Category, Product, SubCategories, User, ProductColor, ProductImage, ProductSizeStock


class RegisterSerializer(ModelSerializer):
    email = EmailField(required=True, )
    password = CharField(write_only=True, required=True, validators=[validate_password, ])

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'full_name')

    def create(self, validated_data):
        user = User.objects.create(
            **validated_data
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


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
