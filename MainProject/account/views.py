import os
import sys
import pickle

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if path not in sys.path:
    sys.path.append(path)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from account.forms import RegistrationForm
from account.forms import EditProfileForm
from account.manage_profile import set_profile_values
from django.contrib.auth.views import login

import functools
import warnings

from django.conf import settings
# Avoid shadowing the login() and logout() views below.
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import resolve_url
from django.template.response import TemplateResponse
from django.urls import reverse
from django.utils.deprecation import RemovedInDjango20Warning
from django.utils.encoding import force_text
from django.utils.http import is_safe_url, urlsafe_base64_decode
from django.utils.six.moves.urllib.parse import urlparse, urlunparse
from django.utils.translation import ugettext as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from tree_db_interface import search_trees, load_trees, search_tree_by_id_list, add_tree
import tree.tree as tree
from search.views import search
from .manage_profile import add_tree_to_profile, get_username_info, add_username, remove_tree_from_profile
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            add_username(form.cleaned_data['username'])
            return HttpResponseRedirect('/account/registerSuccess')

    else:
        form = RegistrationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('account/register.html', token)


def registerSuccess(request):

    return render_to_response('account/registerSuccess.html')


def customLogin(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          extra_context=None, redirect_authenticated_user=False):
        return login(request,
                 template_name,
                 redirect_field_name,
                 authentication_form,
                 extra_context,
                 redirect_authenticated_user)


def loginSuccess(request):
    return render_to_response('account/profile.html')


def profile(request):
    if request.user.is_authenticated:
        username = request.user.username
        profile_values = get_username_info(username)
        if len(profile_values) > 0:
            profile = profile_values.get()

            token = {}
            token.update(csrf(request))
            token['username'] = username
            token['name'] = profile['name']
            token['status'] = profile['status']
            token['dob'] = profile['dob']
            token['gender'] = profile['gender']
            token['email'] = profile['email']

        return render(request, "account/profile.html", token)
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def editProfile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EditProfileForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                status = form.cleaned_data['status']
                dob = form.cleaned_data['dob']
                gender = form.cleaned_data['gender']
                email = form.cleaned_data['email']

                set_profile_values(request.user.username, name, status, dob, gender, email)
                return HttpResponseRedirect('/account/profile')
        else:
            form = EditProfileForm()

        token = {}
        token.update(csrf(request))
        token['form'] = form

        return render(request, "account/editProfile.html", token)
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url="login/")
def home(request):
    return render(request, "account/home.html")



def subscribeTree(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            tree_key = request.POST.get("subscribe", "120391293")

        else:
            tree_key = "120391293"



        trees = search_tree_by_id_list(tree_key)

        if trees:

            add_tree_to_profile(trees, request.user.username)


        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(reverse(customLogin))
def split_list(data, partsCount):
    chunks = [data[x:x + partsCount] for x in range(0, len(data), partsCount)]
    return chunks
def displaySubscribedTrees(request):

    if request.user.is_authenticated:
        user = request.user.username
        info = get_username_info(user)
        info = info[0]

        context = {}
        if info['subscribedTrees'] == '':
            context['tuples'] = '' # will not load any tree's, id's are numbers.
            context['result_objects'] = ''

        else:
            context['tuples'] = search_tree_by_id_list(info['subscribedTrees'])
            context['result_objects'] = load_trees(context['tuples'])


        context['combined_result'] = []
        for i in range(0, len(context['tuples'])):
            if (context['result_objects'][i]['tree'] is None):
                context['result_objects'][i]['tree'] = ''
            else:
                context['result_objects'][i]['tree'] = '/subjects/' + context['tuples'][i]['name'] + '/'
            t = [context['tuples'][i], context['result_objects'][i]]
            context['combined_result'].append(t)
        context['combined_result_4cols'] = split_list(context['combined_result'], 4)
        return render(request, "account/subscribedTrees.html", context)
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def unsubscribeTree(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            id = str(request.POST.get('unsubscribe', 'a'))
        user = request.user.username
        remove_tree_from_profile(id, user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        return render(request, "account/home.html")

def createTreePage(request):
    if request.user.is_authenticated:
        return render(request, "account/createTree.html")
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def add_tree_to_database(request):
    if request.method == 'POST':

        tree_name = request.POST.get('treeName', '')
        tree_category = request.POST.get('category', '')
        tree_subject = request.POST.get('subject', '')
        tree_topic = request.POST.get('topic', '')
        tree_tags = request.POST.get('tags', '')

        x = request.FILES.keys()
        if 'figure' in request.FILES.keys() and 'tree' in request.FILES.keys():
            figure = request.FILES['figure']
            file = request.FILES['tree']


        tree_description = request.POST.get('description', '')

        tree_details = {'name': tree_name, 'category': tree_category, 'subject': tree_subject, 'topic': tree_topic, 'tags': tree_tags}




        path = add_tree(file, figure, tree_description, tree_details)
        return render(request, "account/subscribedTrees.html")

    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

