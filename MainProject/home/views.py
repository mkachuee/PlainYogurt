from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

class Test:
	def __init__(self, A, B):
		self.a = A
		self.b = B

def home(request):
	test = Test(1,2)
	context = {"Test": test}
	return render(request, 'home/home.html',context)
