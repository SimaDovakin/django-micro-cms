from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import LeadCaptureForm
from .models import WebPage, PageSection
from leads.models import WalkIn
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

    if request.method == "POST":
        form = LeadCaptureForm(request.POST)

        device_id = request.COOKIES.get('deviceId')
        if device_id:
            if form.is_valid():
                device = Device.objects.get(pk=device_id)
                lead = form.save(commit=False)

                walk_in = WalkIn(
                    lead=lead,
                    vendor=device.vendor,
                    device=device,
                    currency=device.currency,
                    price=device.price
                )

                lead.save()
                walk_in.save()

                messages.success(request, 'Successfuly sent!')
                return redirect('index')
        else:
            messages.error(request, "Please, select a device!")
    else:
        form = LeadCaptureForm()

    context = {
        'page': page,
        'page_sections': page_sections,
        'page_obj': page_obj,
        'form': form
    }

    return render(request, 'pages/index.html', context)

