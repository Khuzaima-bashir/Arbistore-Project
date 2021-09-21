from rest_framework.serializers import CharField, EmailField, ModelSerializer, SerializerMethodField

from arbistore.models import Category, Product, SubCategory, User


class RegisterSerializer(ModelSerializer):
    email = EmailField(required=True, )
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


class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductsSerializer(ModelSerializer):
    category_id = CategorySerializer()
    sub_category = SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_sub_category(self, obj):
        sub_categories = []
        for sub_category in obj.sub_category.all():
            sub_categories.append({'id': sub_category.id, 'name': sub_category.name})
        return sub_categories


