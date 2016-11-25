import os
import sys
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
from tree_db_interface import search_trees, load_trees
from search.views import search
from .manage_profile import add_tree_to_profile
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
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
    return render_to_response('account/profile.html')

@login_required(login_url="login/")
def home(request):
    return render(request, "account/home.html")

def split_list(data, partsCount):
    chunks = [data[x:x + partsCount] for x in range(0, len(data), partsCount)]
    return chunks
def subscribeTree(request):

    if request.user.is_authenticated:
        context ={}
        if request.method == 'POST':
            tree_key = request.POST.get("subscribe", "120391293")
        else:
            tree_key = "120391293"

        trees = search_trees(tree_key)

        if trees:
            add_tree_to_profile(trees)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(reverse(customLogin))
# def displaySubscribedTrees(request):
#
#
#     context['tuples'] =
#     context['result_objects'] = load_trees(context['tuples'])
#
#     context['combined_result'] = []
#     for i in range(0, len(context['tuples'])):
#         if (context['result_objects'][i]['tree'] is None):
#             context['result_objects'][i]['tree'] = ''
#         else:
#             context['result_objects'][i]['tree'] = '/subjects/' + context['tuples'][i]['name'] + '/'
#         t = [context['tuples'][i], context['result_objects'][i]]
#         context['combined_result'].append(t)
#
#     context['combined_result_4cols'] = split_list(context['combined_result'], 4)