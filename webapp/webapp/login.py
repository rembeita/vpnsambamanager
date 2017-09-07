# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")


def login(request):
       template = loader.get_template('general/index.html')
       #STATIC_URL_ROD = '/static/'
       context = locals()
       #context['STATIC_URL_ROD'] = STATIC_URL_ROD

       context_instance = RequestContext(request)
       return render(request, 'general/index.html', context)


