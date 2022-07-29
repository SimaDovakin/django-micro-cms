from django.contrib import admin

from .models import Lead, WalkIn


class LeadAdmin(admin.ModelAdmin):
    pass


class WalkInAdmin(admin.ModelAdmin):
    pass


admin.site.register(Lead, LeadAdmin)
admin.site.register(WalkIn, WalkInAdmin)

