# coding: utf-8
"""
    Registering entities and their custom registration forms in
    django admin interface
"""
from django.contrib import admin
from django.forms import ModelForm
from TestTask.apps.Spittler.widgets.SpittleTextarea import SpittleTextarea
from models import Spittle


class SpittleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SpittleForm, self).__init__(*args, **kwargs)
        self.fields['_text'].widget = SpittleTextarea()

    class Meta:
        model = Spittle


class SpittleAdmin(admin.ModelAdmin):
    form = SpittleForm


admin.site.register(Spittle, SpittleAdmin)
