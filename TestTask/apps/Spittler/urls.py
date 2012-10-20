# coding: utf-8
"""
    Spittler Application url mappings
"""

from django.conf.urls import patterns, url
from TestTask.apps.Spittler import views


urlpatterns = patterns('',
                       url(r'^$', views.list_spittles, name="list_spittles"),
                       url(r'^add/$', views.add_spittle, name="add_spittle"),
                       )
