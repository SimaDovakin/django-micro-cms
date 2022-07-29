from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render

from .models import WebPage, PageSection
from products.models import Device


def index(request):
    current_site = get_current_site(request)

    page = WebPage.objects.get(site=current_site)
    page_sections = PageSection.objects.filter(
        page=page,
        is_active=True
    ).order_by('order')
    devices = Device.objects.filter(
        page=page
    ).select_related('vendor')

    context = {
        'page': page,
        'page_sections': page_sections,
        'devices': devices
    }

    return render(request, 'pages/index.html', context)

