from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as CoreValidationException
from rest_framework.serializers import CharField, EmailField, ModelSerializer, SerializerMethodField, ValidationError, \
    StringRelatedField

from arbistore.models import Category, Product, SubCategory, User


class RegisterSerializer(ModelSerializer):
    email = EmailField(required=True,)
    password = CharField(write_only=True, required=True)

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

    def validate_password(self, password):
        try:
            validate_password(password)
        except CoreValidationException:
            raise ValidationError(validate_password(password))


class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    sub_category = StringRelatedField(many=True)

    class Meta:
        model = Category
        fields = ('name', 'sub_category')


class ProductCategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('name',)


class ProductsSerializer(ModelSerializer):
    category_id = ProductCategorySerializer()
    sub_category = StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = '__all__'
