from django.conf.urls import url
from . import views as accView
from django.contrib.auth import views as authView
from acc import forms

urlpatterns = [
    url(r'^$', accView.home, name='home'),
    url(r'^login/$', accView.customLogin, {'template_name': 'acc/login.html', 'authentication_form': forms.LoginForm},
        name='login'),
    url(r'^loginSuccess/$', accView.loginSuccess, name='loginSuccess'),
    url(r'^logout/$', authView.logout, {'next_page': 'login'}),
    url(r'^register/$', accView.register, name='register'),
    url(r'^registerSuccess/$', accView.registerSuccess, name='registerSuccess')
]
