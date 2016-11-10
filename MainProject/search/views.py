# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template.context_processors import csrf
from dbaccess import search_tree

from django.http import HttpResponse
from django.template import loader

# Create your views here.
def search(request):
	title = "Search Results"

	query = {}
	query['title'] = "Query"
	search = "Machine Learning"
	query['search'] = search
	result = search_tree(search)
	query['result'] = result

	context = {}
	context.update(csrf(request))
	context['title']=title;
	context['query']=query;

	return render(request, 'search/search.html', context)
