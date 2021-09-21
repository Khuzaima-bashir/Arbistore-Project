from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models import BooleanField, CASCADE, CharField, DateTimeField, EmailField,\
    Model, ForeignKey, ImageField, IntegerField, TextField, ManyToManyField

from arbistore.enum import Choices


class UserManager(BaseUserManager):

    def create_user(self, username, password=None):
        new_user = self.model(username=username)
        new_user.set_password(password)
        new_user.save(using=self._db)
        return new_user

    def create_superuser(self, username, password):
        new_user = self.create_user(username=username, password=password, )
        new_user.is_admin = True
        new_user.is_staff = True
        new_user.is_superuser = True
        new_user.save(using=self._db)
        return new_user


class User(AbstractBaseUser):
    username = CharField(max_length=200, unique=True)
    email = EmailField(max_length=300, unique=True)
    full_name = CharField(max_length=300, unique=True)
    address = CharField(max_length=300)
    is_admin = BooleanField(default=False)
    is_staff = BooleanField(default=False)
    is_superuser = BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = ['username', 'email', 'full_name']

    objects = UserManager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Brand(Model):
    name = CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class BaseModel(Model):
    created_on = DateTimeField(verbose_name='created on', auto_now_add=True)
    updated_on = DateTimeField(verbose_name='date joined', auto_now_add=True)

    class Meta:
        abstract = True


class Category(Model):
    name = CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class ProductDetail(Model):
    color = CharField(max_length=20, choices=Choices.ColorChoice.value)
    stock = IntegerField(blank=False)
    size = CharField(max_length=20, choices=Choices.Sizes.value)


class SubCategory(Model):
    name = TextField(max_length=200)
    category = ForeignKey(Category, on_delete=CASCADE, default=1)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = CharField(max_length=200, unique=True)
    gender = CharField(max_length=20, choices=[("Male", 'Male'), ("Female", 'Female')])
    description = TextField(max_length=500)
    category_id = ForeignKey(Category, on_delete=CASCADE)
    brand_id = ForeignKey(Brand, on_delete=CASCADE)
    product_detail = ForeignKey(ProductDetail, on_delete=CASCADE, default=1)
    sub_category = ManyToManyField(SubCategory)

    def __str__(self):
        return self.name


class ProductImage(Model):
    product_detail_id = ForeignKey(ProductDetail, on_delete=CASCADE)
    images = ImageField(upload_to='media/')
