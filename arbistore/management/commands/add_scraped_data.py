from json import load
from random import randint

from django.core.management.base import BaseCommand

from arbistore.models import Brand, Category, Product, ProductColor, ProductSizeStock, ProductImage, SubCategories
from arbistore.constants import COLORSCHOICES


def create_category(category_name):
    if len(Category.objects.filter(name=category_name)) == 0:
        category = Category(name=category_name)
        category.save()
    else:
        category = Category.objects.get(name=category_name)
    return category


def create_sub_categories(category, subcategories):
    sub_categories = []
    for sub_category_name in subcategories:
        if len(SubCategories.objects.filter(name=sub_category_name)) == 0:
            sub_category = SubCategories(name=sub_category_name, category=category)
            sub_category.save()
            sub_categories.append(sub_category)
        else:
            sub_category = SubCategories.objects.get(name=sub_category_name)
            sub_categories.append(sub_category)
    return sub_categories


def create_product(product_item, category, sub_categories, brand):
    product = Product(name=product_item['Name'], gender=product_item['product_gender'],
                      price=int(float(product_item['Price'])), full_description=product_item['Description'],
                      category_name=category, brand=brand)
    product.save()
    product.sub_categories.set(sub_categories)
    product.save()

    return product


def create_brand(brand_name):
    try:
        brand = Brand(name=brand_name)
        brand.save()
    except:
        brand = Brand.objects.get(name=brand_name)
    return brand


def create_product_colors(colors, product):
    product_colors = []
    for product_color in colors:
        product_color_list = product_color.split(' ')

        for color in product_color_list:
            color = color.split('/')[0]
            if color.lower() in COLORSCHOICES:
                new_product_color = ProductColor(color=color, product=product)

        new_product_color.save()
        product_colors.append(new_product_color)
    return product_colors


def create_product_sizes_stock(product_colors, sizes):
    for product_color in product_colors:

        for current_size in sizes:
            product_size_stock = ProductSizeStock(size=current_size, stock=randint(0, 100),
                                                  product_color=product_color)
            product_size_stock.save()


def add_product_images(product_colors, product_images):
    for image_index_finder in range(len(product_colors)):
        image_path = product_images[image_index_finder]['url']
        product_image = ProductImage(image=image_path, product_color=product_colors[image_index_finder])
        product_image.save()


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_data_file = open('ProductData.json', 'r')
        product_data = load(product_data_file)

        brand = create_brand("Musto")

        for product_item in product_data:
            category = create_category(product_item['Category'])
            sub_categories = create_sub_categories(category, product_item['Sub Categories'])
            product = create_product(product_item, category, sub_categories, brand)
            product_colors = create_product_colors(product_item['Colors'], product)
            create_product_sizes_stock(product_colors, product_item['Sizes'])
            add_product_images(product_colors, product_item['images'])
