from django.contrib.auth.models import AbstractUser
from django.db import models


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
    name = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categories')

    def __str__(self):
        return self.name


class Product(TimeStampModel):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    price = models.IntegerField(blank=False)
    full_description = models.TextField(max_length=500)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_name")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="brand")
    sub_categories = models.ManyToManyField(SubCategories)

    def __str__(self):
        return self.name


class ProductColor(TimeStampModel):
    color = models.CharField(max_length=100, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_detail')


class ProductSizeStock(TimeStampModel):
    size = models.CharField(max_length=200)
    stock = models.IntegerField(blank=False)
    product_color = models.ForeignKey(ProductColor, on_delete=models.CASCADE, related_name="product_size_stock")


class ProductImage(TimeStampModel):
    image = models.ImageField(upload_to='media/', max_length=255)
    product_color = models.ForeignKey(ProductColor, on_delete=models.CASCADE, related_name='product_color_image')
