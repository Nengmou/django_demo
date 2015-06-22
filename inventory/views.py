from django.shortcuts import get_object_or_404, get_list_or_404, render
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


@login_required
def inventory_index(request):
    items = Inventory.objects.order_by('-id')
    return render(request, 'inventory/inventory_index.html', {'items': items})


@login_required
def inventory_detail(request, inv_id):
    inventory = get_object_or_404(Inventory, pk=inv_id)
    return render(request, 'inventory/inventory_detail.html', {'item': inventory})


@login_required
def shipment_index(request):
    items = Shipment.objects.order_by('-id')
    return render(request, 'inventory/shipment_index.html', {'items': items})


@login_required
def shipment_detail(request, s_id):
    shipment = get_object_or_404(Shipment, pk=s_id)
    return render(request, 'inventory/shipment_detail.html', {'item': shipment})


@login_required
def report_low_total(request):
    items = get_list_or_404(Inventory, on_floor_quantity__lte=500)
    return render(request, 'inventory/report_low_inventory.html', {'items': items, 'title': 'Low Inventory Report'})


@login_required
def report_low_on_floor(request):
    items = get_list_or_404(Inventory, on_floor_quantity__lte=500)
    return render(request, 'inventory/report_low_inventory.html', {'items': items, 'title': 'Low on Floor Report'})


@login_required
def report_low_in_warehouse(request):
    items = get_list_or_404(Inventory, in_warehouse_quantity__lte=500)
    return render(request, 'inventory/report_low_inventory.html', {'items': items, 'title': 'Low in Warehouse Report'})
