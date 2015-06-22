from django.conf.urls import patterns, url

from inventory import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^vendors/$', views.vendor_index, name='vendor.index'),
    url(r'^vendors/(?P<v_id>\d+)/$', views.vendor_detail, name='vendor.detail'),
    url(r'^inventories/$', views.inventory_index, name='inventory.index'),
    url(r'^inventories/(?P<inv_id>\d+)/$', views.inventory_detail, name='inventory.detail'),
    url(r'^shipments/$', views.shipment_index, name='shipment.index'),
    url(r'^shipments/(?P<s_id>\d+)/$', views.shipment_detail, name='shipment.detail'),
    url(r'^report_low_total/$', views.report_low_total, name='low.total'),
    url(r'^report_low_on_floor/$', views.report_low_on_floor, name='low.on.floor'),
    url(r'^report_low_in_warehouse/$', views.report_low_in_warehouse, name='low.in.warehouse'),
)
