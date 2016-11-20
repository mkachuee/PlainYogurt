# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

import pickle
import os
import json

def allSubjects(request):
	return render(request, 'subjects/subjects.html')


def specificSubject(request, subjectName):
	# get subjectName from database and put into context
	module_dir = os.path.dirname(__file__)  # get current directory
	data_path = os.path.join(module_dir, 'tree_list.pkl')
	with open(data_path, 'rb') as f:
		data = pickle.load(f)

	data_in_json = json.dumps(data)
	context = {'subjectName': subjectName, 'data': data_in_json}
	return render(request, 'subjects/specificSubject.html', context)
