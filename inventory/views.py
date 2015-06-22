from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from inventory.models import *


def index(request):
    return render(request, 'inventory/index.html')


@login_required
def vendor_index(request):
    items = Vendor.objects.order_by('-id')[:5]
    return render(request, 'inventory/vendor_index.html', {'items': items})


@login_required
def vendor_detail(request, v_id):
    vendor = get_object_or_404(Vendor, pk=v_id)
    return render(request, 'inventory/vendor_detail.html', {'item': vendor})

