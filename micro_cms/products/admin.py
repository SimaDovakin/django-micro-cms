from django.contrib import admin

from .models import Country, City, Vendor, Device


class CountryAdmin(admin.ModelAdmin):
    pass


class CityAdmin(admin.ModelAdmin):
    pass


class VendorAdmin(admin.ModelAdmin):
    pass


class DeviceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Device, DeviceAdmin)

