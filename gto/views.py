__author__ = 'taksenov'
# coding=utf-8

# imports
from django.db import connection
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context, RequestContext

from django.views.generic import DetailView, TemplateView
from .models import menu_main, menu_item

class GtoDocumentsList(TemplateView):
    template_name = 'gto.html'

    def get_context_data(self, **kwargs):
        context = super(StructureDocumentsList, self).get_context_data(**kwargs)
        context['menuMain'] = menu_main.objects.all()
        context['menuItem'] = menu_item.objects.all()
        return context
