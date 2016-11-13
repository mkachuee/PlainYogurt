# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template.context_processors import csrf
from dbaccess import search_tree
from dbaccess import get_query

from django.http import HttpResponse
from django.template import loader


# Create your views here.
def search(request):
    q = ""
    if request.method == 'GET':
        q = request.GET.get('q','')
    title = "Search"

    query = {}
    query['title'] = "Query:" + q
    search = "Machine Learning"
    query['search'] = q
    if q:
        result = search_tree(q)
    else:
        result = ""
    query['result'] = result
    if q:
        queryObject = get_query(q, 'name')
    else:
        queryObject = ""
    query['object'] = queryObject

    context = {}
    context.update(csrf(request))
    context['title'] = title;
    context['query'] = query;

    return render(request, 'search/search.html', context)
