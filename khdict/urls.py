from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'khdict.views.index'),
    url(r'^q/(?P<key>.*)?$', 'khdict.views.query'),
)
