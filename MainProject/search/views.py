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
        q = request.GET.get('q', '')

    query = {}
    query['title'] = "Query:" + q
    context = {}
    context.update(csrf(request))
    if q:
        querySetResult = search_trees(q)
        result = load_trees(querySetResult)
        query['result'] = result
        queryObject = get_query(q, 'name')
        query['object'] = queryObject
        query['count1'] = range(0, 3)
        query['count2'] = range(0, 4)
        resultCount = 13
        querySetResultTable = {}
        c = 0;
        breakLoopFlag = False;
        while True:
            querySetResultRow = {}
            for i in range(0, 4):
                """Add result[i] to querySetResultRow"""
                """Add querySetResultRow to querySetResultTable"""
                c = c + 1
                if (c >= resultCount):
                    breakLoopFlag = True
                    break
            if (breakLoopFlag):
                break

        context['hasQuery'] = True
        context['q'] = q
        context['query'] = query
        context['result'] = result
        context['tuple'] = querySetResult

        if len(querySetResult)>0:
            context['hasResult'] = True
            context['firstTuple'] = querySetResult[0]
            context['firstResult'] = result[0]
        else:
            context['hasResult'] = False
            context['firstTuple'] = {}
            context['firstResult'] = {}
    else:
        context['hasQuery'] = False
        context['q'] = q
        context['query'] = {}
        context['result'] = {}
        context['tuple'] = {}
        context['hasResult'] = False
        context['firstTuple'] = {}
        context['firstResult'] = {}
    return render(request, 'search/search.html', context)
