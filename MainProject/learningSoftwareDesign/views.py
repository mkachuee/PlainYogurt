# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

# Create your views here.
def learningSoftwareDesign(request):
	return render(request, 'learningSoftwareDesign/learningSoftwareDesign.html')
