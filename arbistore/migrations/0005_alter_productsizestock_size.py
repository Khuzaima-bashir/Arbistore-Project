# Generated by Django 3.2.6 on 2021-10-12 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arbistore', '0004_alter_product_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsizestock',
            name='size',
            field=models.CharField(max_length=20),
        ),
    ]
