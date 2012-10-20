# coding: utf-8
"""
    Views of Spittler Application
"""
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from django.shortcuts import render_to_response
from django.template import RequestContext
from TestTask.apps.Spittler.forms.spittle import AddSpittleForm
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
