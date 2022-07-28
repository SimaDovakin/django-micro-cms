from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.sites.shortcuts import get_current_site
from django.db import models


def _save_image(instance, filename):
    return f"section_image/{get_current_site().id}_{instance.pk}_{filename}"


class WebPage(models.Model):
    title = models.CharField(max_length=64)
    site = models.OneToOneField(Site, on_delete=models.CASCADE)

    # Model managers
    objects = models.Manager()
    on_site = CurrentSiteManager()

    def __str__(self):
        return self.title


class PageSection(models.Model):
    title = models.CharField(max_length=64)
    image = models.ImageField(
        upload_to=_save_image,
        blank=True
    )
    html_content = models.TextField()
    order = models.PositiveSmallIntegerField(default=0)
    page = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

