from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_protect
from django.conf import settings

class Test:
    def __init__(self, A, B):
        self.a = A
        self.b = B


def home(request):
    test = Test(1, 2)
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = ""
        message = message + "from: " + name
        message = message + "\nemail: " + email
        message = message + "\nphone: " + phone
        message = message + "\nmessage:\n" + request.POST['message']

        send_mail('Contact Message',message,settings.DEFAULT_FROM_EMAIL,['paul.m.kim321@gmail.com'],fail_silently=False)

        context = {"Submitted": True, "name":name}
	
    else:
        context = {"submitted": False}
    return render(request, 'home/index.html', context)

