from django.contrib.sites.shortcuts import get_current_site
from django.core.paginator import Paginator
from django.shortcuts import render

from .forms import LeadCaptureForm
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
    ).order_by('name').select_related('vendor')

    paginator = Paginator(devices, 12)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    form = LeadCaptureForm()

    context = {
        'page': page,
        'page_sections': page_sections,
        'page_obj': page_obj,
        'form': form
    }

    return render(request, 'pages/index.html', context)

