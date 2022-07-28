from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.validators import RegexValidator
from django.db import models

from pages.models import WebPage


def _save_image(instance, filename):
    return f"product_image/{get_current_site().id}_{instance.pk}_{filename}"


class Country(models.Model):
    name = models.CharField(max_length=128)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=256)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=128)
    phone_number = models.CharField(
        max_length=17,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message=(
                    "Phone number must be entered in the format:"
                    "'+999999999'. Up to 15 digits is allowed."
                ),
                code='invalid_phone_number'
            )
        ]
    )
    address = models.CharField(max_length=256)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Device(models.Model):
    CURRENCY = [
        ('USD', 'United States dollar'),
        ('EUR', 'Euro'),
        ('UAH', 'Ukrainian hryvnia')
    ]

    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to=_save_image, blank=True)
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY,
        default='USD'
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    page = models.ForeignKey(WebPage, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

