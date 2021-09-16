from django.contrib import admin

from arbistore.models import Brand, Category, ImagesDetails,  Products, ProductsDetails, SubCategory, User


class ImageInlineAdmin(admin.StackedInline):
    extra = 1
    model = ImagesDetails


class ImageAdmin(admin.ModelAdmin):
    inlines = [ImageInlineAdmin]


admin.site.register(User)
admin.site.register(Products)
admin.site.register(Category)
admin.site.register(ProductsDetails, ImageAdmin)
admin.site.register(SubCategory)
admin.site.register(Brand)
