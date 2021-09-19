from django.contrib import admin
from django.contrib.admin import StackedInline, ModelAdmin

from arbistore.models import Brand, Category, Product, ProductDetail, ProductImage, SubCategory, User


class ProductImageInline(StackedInline):
    extra = 1
    model = ProductImage


class ProductImageAdmin(ModelAdmin):
    inlines = [ProductImageInline]


admin.site.register(User)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductDetail, ProductImageAdmin)
admin.site.register(SubCategory)
admin.site.register(Brand)
