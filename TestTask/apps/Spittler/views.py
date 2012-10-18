# coding: utf-8
"""
    Views of Spittler Application
"""

from django.shortcuts import render_to_response
from django.template import RequestContext
from TestTask.apps.Spittler.models import Spittle


def list_spittles(request):
    """ Lists all current messages(i.e. spittles) on page """

    spittles = Spittle.objects.all()
    context = {
        'spittles': spittles,
    }
    return render_to_response('spittles.html',
                              RequestContext(request, context)
                              )