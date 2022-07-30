from django.core.validators import RegexValidator
from django.db import models

from products.models import (
    Country,
    City,
    Vendor,
    Device
)


class Lead(models.Model):
    STATUSES = [
        (0, 'Pending'),
        (1, 'In-progress'),
        (2, 'Converted'),
        (3, 'Rejected')
    ]

    email = models.EmailField(primary_key=True)
    name = models.CharField(max_length=256)
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
    referral_code = models.CharField(max_length=8, blank=True, default="")
    status = models.PositiveSmallIntegerField(choices=STATUSES, default=0)

    def __str__(self):
        return self.name


class WalkIn(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    currency = models.CharField(max_length=3)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField(auto_now_add=True)
    token_number = models.PositiveIntegerField()

    def __str__(self):
        return self.lead.name

    def save(self, *args, **kwargs):
        most_recent_walkin = WalkIn.objects.filter(
            vendor=self.vendor
        ).order_by('-created_on').first()
        if most_recent_walkin:
            self.token_number = most_recent_walkin.token_number + 1
        else:
            self.token_number = 1
        super().save(*args, **kwargs)

