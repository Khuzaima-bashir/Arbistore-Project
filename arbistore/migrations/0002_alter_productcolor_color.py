# Generated by Django 3.2.6 on 2021-10-12 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arbistore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcolor',
            name='color',
            field=models.CharField(max_length=100),
        ),
    ]
