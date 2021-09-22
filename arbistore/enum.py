from enum import Enum


class ColorChoices(Enum):
    Colors = [
        ('Black', 'Black'),
        ('Blue', 'Blue'),
        ('Red', 'Red'),
        ('Yellow', 'Yellow'),
        ('Purple', 'Purple'),
        ('White', 'White'),
        ('Green', 'Green')
    ]


class SizeChoices(Enum):
    Sizes = [
        ('XL', 'XL'),
        ('L', 'L'),
        ('M', 'M'),
        ('S', 'S')
    ]
