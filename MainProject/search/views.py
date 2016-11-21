# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
import os
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if path not in sys.path:
    sys.path.append(path)

from django.shortcuts import render
from django.template.context_processors import csrf
from dbaccess import get_query
from tree_db_interface import search_trees, load_trees
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import loader

"""
Change this constant to false if you don't want to use fake data
"""
DEBUG_MODE_USE_FAKE_DATA = False

def debug_fake_data():
    combined_result = []

    for i in range(0,15):
        t = []
        data = {}
        data["name"] = "Computer Graphics"
        t.append(data)
        data = {}
        data["description"] = "Drawing with computers"
        data["image"] = "subjects/img/ComputerGraphic.jpg"
        t.append(data)
        combined_result.append(t)
        t = []
        data = {}
        data["name"] = "Machine Learning"
        t.append(data)
        data = {}
        data["description"] = "learning with machine"
        data["image"] = "subjects/img/MachineLearning.jpg"
        t.append(data)
        combined_result.append(t)
        t = []
        data = {}
        data["name"] = "Software Design"
        t.append(data)
        data = {}
        data["description"] = "design a software"
        data["image"] = "subjects/img/SoftWareDesign.jpg"
        t.append(data)
        combined_result.append(t)

    return combined_result

def split_list(data, partsCount):
    chunks = [data[x:x + partsCount] for x in range(0, len(data), partsCount)]
    return chunks

@csrf_protect
def search(request):
    context = {}
    if request.method == 'POST':
        context['q'] = request.POST.get("q", "hello")
    else:
        context['q'] = ""

    q = context['q']
    context['tuples'] = search_trees(q)
    context['result_objects'] = load_trees(context['tuples'])

    context['combined_result'] = []
    for i in range(0, len(context['tuples'])):
        t = [context['tuples'][i], context['result_objects'][i]]
        context['combined_result'].append(t)

    if (DEBUG_MODE_USE_FAKE_DATA):
        context['combined_result'] = debug_fake_data()

    context['combined_result_4cols'] = split_list(context['combined_result'], 4)
    return render(request, 'search/search.html', context)
