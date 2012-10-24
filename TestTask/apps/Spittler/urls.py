# coding: utf-8
"""
    spittler Application url mappings
"""

from django.conf.urls import patterns, url
from TestTask.apps.spittler import views


urlpatterns = patterns('',
                       url(r'^$', views.list_spittles, name="list_spittles"),
                       url(r'^add/$', views.add_spittle, name="add_spittle"),
                       url(r'^widget/$', views.get_widget, name="get_widget"),
                       url(r'^download/$', views.download_widget, name="download_widget"),
                       url(r'^rest/spittle/$', views.get_spittle_json, name="rest_api"),
                       )
