from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class Manager(BaseUserManager):

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
    username = models.CharField(null=False, max_length=200, unique=True)
    email = models.EmailField(null=False, max_length=300, unique=True)
    full_name = models.CharField(null=False, max_length=300, unique=True)
    address = models.CharField(null=False, max_length=300)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = ['username', 'email', 'full_name']

    objects = Manager()

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Category(models.Model):
    name = models.CharField(null=False, max_length=200, unique=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(null=False, max_length=200, unique=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(null=False, max_length=200, unique=True)
    gender = models.CharField(null=False, max_length=20, choices=[("Male", 'Male'), ("Female", 'Female')])
    product_description = models.CharField(null=False, max_length=500)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProductsDetails(models.Model):
    color = models.CharField(null=False, max_length=20, choices=[
        ('Black', 'Black'),
        ('Blue', 'Blue'),
        ('Red', 'Red'),
        ('Yellow', 'Yellow'),
        ('Purple', 'Purple'),
        ('White', 'White'),
        ('Green', 'Green')])
    stock = models.IntegerField(null=False)
    size = models.CharField(null=False, max_length=20, choices=[('XL', 'XL'), ('L', 'L'), ('M', 'M'), ('S', 'S')])
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)


class ImagesDetails(models.Model):
    product_details_id = models.ForeignKey(ProductsDetails, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='media/')


class SubCategory(models.Model):
    name = models.CharField(null=False, max_length=200)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    products_id = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
