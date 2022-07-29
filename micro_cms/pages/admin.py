from django.contrib import admin

from .models import WebPage, PageSection


class WebPageAdmin(admin.ModelAdmin):
    pass


class PageSectionAdmin(admin.ModelAdmin):
    pass


admin.site.register(WebPage, WebPageAdmin)
admin.site.register(PageSection, PageSectionAdmin)

