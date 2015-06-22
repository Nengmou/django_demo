from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('inventory.urls', namespace="inventories")),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
