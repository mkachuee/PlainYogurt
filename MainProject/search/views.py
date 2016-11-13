# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template.context_processors import csrf
from dbaccess import search_tree
from dbaccess import get_query
from tree_db_interface import search_trees, load_trees

from django.http import HttpResponse
from django.template import loader


# Create your views here.
def search(request):
    q = ""
    if request.method == 'GET':
        q = request.GET.get('q','')

    query = {}
    query['title'] = "Query:" + q

    if q:
        querySetResult = search_trees(q)
        result = load_trees(querySetResult)
    else:
        result = ""
    query['result'] = result

    if q:
        queryObject = get_query(q, 'name')
    else:
        queryObject = ""
    query['object'] = queryObject

    query['count1'] = range(0, 3)
    query['count2'] = range(0, 4)
    querySetResultTable = {}


    context = {}
    context.update(csrf(request))
    context['query'] = query
    context['result'] = result
    context['tuple'] = querySetResult
    context['firstTuple'] = querySetResult[0]
    context['firstResult'] = result[0]

    return render(request, 'search/search.html', context)
