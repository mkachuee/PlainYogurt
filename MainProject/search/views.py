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

    return render(request, 'search/search.html', context)

