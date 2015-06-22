from django.contrib import admin
from inventory.models import *

# Register your models here.
admin.site.register(Vendor)
admin.site.register(Inventory)
admin.site.register(Shipment)