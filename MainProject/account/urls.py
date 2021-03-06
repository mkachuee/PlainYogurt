from django.conf.urls import url
from django.contrib.auth import views as authView
from account import forms
from account import views
urlpatterns = [
    url(r'^login/$', views.customLogin, {'template_name': 'account/login.html', 'authentication_form': forms.LoginForm},
        name='login'),
    url(r'^loginSuccess/$', views.loginSuccess, name='loginSuccess'),
    url(r'^subscribe/$', views.subscribeTree, name='subscribeTree'),
    url(r'^unsubscribe/$', views.unsubscribeTree, name='unsubscribeTree'),
    url(r'^mytrees/$', views.displaySubscribedTrees, name='displaySubscribedTrees'),
    url(r'^logout/$', authView.logout, {'next_page': 'home'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^registerSuccess/$', views.registerSuccess, name='registerSuccess'),
    url(r'createTree/$', views.createTreePage, name='createTreePage'),
    url(r'submitTree/$', views.add_tree_to_database, name='submitTree'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^editProfile/$', views.editProfile, name='editProfile')
    ]

