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
	
	# TODO: remove the next 3 lines and replace data with the {path,content} dictionary for the correct subject
	# data_path = os.path.join(module_dir, 'example_cnn.pkl')
	data_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + '/static' + '/TreeFiles/' + subjectName + '/tree.pkl'
	with open(data_path, 'rb') as f:
		data = pickle.load(f)

	#data['contents'][0] = {'name':'name 1', 'description':'des1', 'links':[{link:'//http',name:'wiki'}]}
	for key1,value1 in data['contents'].items():
		for key2,value2 in value1.items():
			if(key2 == "links"):
				for i in range(len(value2)):
					for key4,value4 in value2[i].items():
						data['contents'][key1][key2][i][key4] = value4.replace('"','')
						#data['contents'][key1][key2][i][key4] = value4.replace('\\n',' ')
			else:
				data['contents'][key1][key2] = value2.replace('"','')
				#data['contents'][key1][key2] = value2.replace('\\n',' ')

	data_in_json = json.dumps(data)
	subjectName = data['contents'][0]['name']
	context = {'subjectName': subjectName, 'data': data_in_json}
	return render(request, 'subjects/specificSubject.html', context)
