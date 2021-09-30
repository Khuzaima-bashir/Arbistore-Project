from django.contrib.auth.models import AbstractUser
from django.db import models

from arbistore.constants import COLORSCHOICES, SIZESCHOICES, GENDERSCHOICES


class User(AbstractUser):
    full_name = models.CharField(max_length=200)
    address = models.TextField(max_length=350)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = ['username', 'email', 'full_name', 'address']


class TimeStampModel(models.Model):
    created_on = models.DateTimeField(verbose_name='created on', auto_now_add=True)
    updated_on = models.DateTimeField(verbose_name='Updated Last', auto_now=True)

    class Meta:
        abstract = True


class Brand(TimeStampModel):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Category(TimeStampModel):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class SubCategories(TimeStampModel):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categories')

    def __str__(self):
        return self.name


class Product(TimeStampModel):
    name = models.CharField(max_length=100, unique=True)
    gender = models.IntegerField(choices=GENDERSCHOICES)
    price = models.IntegerField(blank=False)
    short_description = models.CharField(max_length=100)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_name")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="brand")
    sub_categories = models.ManyToManyField(SubCategories)

    def __str__(self):
        return self.name


class ProductDetail(TimeStampModel):
    color = models.CharField(max_length=200, blank=False, choices=COLORSCHOICES)
    full_description = models.TextField(max_length=500)
    size = models.CharField(max_length=20, choices=SIZESCHOICES)
    stock = models.IntegerField(blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_detail')


class ProductImage(TimeStampModel):
    image = models.ImageField(upload_to='media/')
    product_detail = models.ForeignKey(ProductDetail, on_delete=models.CASCADE, related_name="product_images")
