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
        fields = ('name',)


class CategorySerializer(ModelSerializer):
    sub_category = SerializerMethodField()

    class Meta:
        model = Category
        fields = "__all__"

    def get_sub_category(self, obj):
        return SubCategory.objects.filter(category=obj.id,
                                          ).values_list('name', flat=True)


class ProductsSerializer(ModelSerializer):
    category_id = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'
