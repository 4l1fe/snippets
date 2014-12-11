from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login$', login),
    url(r'^success$', TemplateView.as_view(template_name='success.html')),
    url(r'^admin/', include(admin.site.urls)),
)
