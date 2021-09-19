from rest_framework.serializers import CharField, EmailField, ModelSerializer

from arbistore.models import Category, Product, SubCategory, User


class RegisterSerializer(ModelSerializer):
    email = EmailField(required=True,)
    password = CharField(write_only=True, required=True)
    password2 = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'full_name', 'address')

    def create(self, validated_data):
        user = User.objects.create(
            **validated_data
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProductsSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('name')


class SubCategorySerializer(ModelSerializer):

    class Meta:
        model = SubCategory
        fields = ('name')
