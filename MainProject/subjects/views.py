# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def allSubjects(request):
    return render(request, 'subjects/subjects.html')


def specificSubject(request, subjectName):
    # get subjectName from database and put into context
    context = {'subjectName': subjectName, 'subjectID': '1'}
    return render(request, 'subjects/specificSubject.html', context)
