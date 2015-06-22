from django.conf.urls import patterns, url

from inventory import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^vendors/$', views.vendor_index, name='vendor.index'),
    url(r'^vendors/(?P<v_id>\d+)/$', views.vendor_detail, name='vendor.detail'),
)
