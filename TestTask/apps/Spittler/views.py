# coding: utf-8
"""
    Views of Spittler Application
"""

from django.shortcuts import render_to_response
from django.template import RequestContext
from TestTask.apps.Spittler.models import Spittle


def list_spittles(request):
    """ Lists all current messages(i.e. spittles) on page """

    identities = Spittle.objects.values_list('_slug', flat=True)
    context = {
        'identities': identities,
    }
    return render_to_response('spittles.html',
                              RequestContext(request, context)
                              )