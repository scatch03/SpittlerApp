from django.conf.urls import patterns, include, url

from django.contrib import admin
from TestTask.apps.spittler import urls

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include(urls)),
                       )
