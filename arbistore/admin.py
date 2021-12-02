from django.contrib import admin
from django.contrib.admin import StackedInline, ModelAdmin

from arbistore.models import Brand, Category, Product, ProductColor, ProductImage, ProductSizeStock, SubCategories, User


class ProductImageInline(StackedInline):
    extra = 1
    model = ProductImage


class ProductImageAdmin(ModelAdmin):
    inlines = [ProductImageInline]


admin.site.register(User)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductColor, ProductImageAdmin)
admin.site.register(ProductSizeStock)
admin.site.register(SubCategories)
admin.site.register(Brand)
