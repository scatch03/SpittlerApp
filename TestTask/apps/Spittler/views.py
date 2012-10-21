# coding: utf-8
"""
    Views of Spittler Application
"""

import json
import os
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.servers.basehttp import FileWrapper
from TestTask.apps.Spittler.forms.spittle import AddSpittleForm
from TestTask.apps.Spittler.models import Spittle
from TestTask.libs.utils import get_protocol
from TestTask.settings import PROJECT_DIR, MEDIA_ROOT


def list_spittles(request):
    """ Lists all current messages(i.e. spittles) on page """

    identities = Spittle.objects.values_list('_slug', flat=True)
    context = {
        'identities': identities,
    }
    return render_to_response('spittles.html',
                              RequestContext(request, context)
                              )


def add_spittle(request):
    """ Adds spittle to current spittle list """

    if request.method == 'POST':
        form = AddSpittleForm(request.POST)
        if form.is_valid():
            spittle = Spittle()
            spittle.message = form.cleaned_data['message']
            spittle.title = form.cleaned_data['subject']
            Spittle.save(spittle)
            return HttpResponseRedirect(reverse('list_spittles'))
    else:
        form = AddSpittleForm()

    return render_to_response('add_spittle.html',
                              RequestContext(request, {'form': form})
                              )


def get_spittle_json(request):
    """ Plucks random spittle """

    callback = request.GET.get('callback', '')
    try:
        spittle = Spittle.objects.order_by('?')[0].get_public_representation()
    except IndexError:
        spittle = {}

    return HttpResponse(callback + '(' + json.dumps(spittle) + ')',
                        mimetype="application/json")


def get_widget(request):
    return render_to_response('get_spittle_widget.html',
                              RequestContext(request, {}))


def download_widget(request):
    path = os.path.join(MEDIA_ROOT, 'spittler_widget.js')
    widget_file = open(path).read()
    widget_file = widget_file.replace('$$HOST$$', request.get_host())
    widget_file = widget_file.replace('$$PROTOCOL$$', get_protocol(request))
    response = HttpResponse(widget_file,
                            content_type='application/javascript')
    response['Content-Disposition'] = 'attachment; filename=SpittleWidget.js'

    return response


