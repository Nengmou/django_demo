from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from inventory.models import *


def index(request):
    return render(request, 'inventory/index.html')


def vendor_index(request):
    items = Vendor.objects.order_by('-id')[:5]
    return render(request, 'inventory/vendor_index.html', {'items': items})


def vendor_detail(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    return render(request, 'inventory/vendor_detail.html', {'item': vendor})
