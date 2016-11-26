import os
import sys
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if path not in sys.path:
    sys.path.append(path)
from home.models import TreeInfo
from .models import Profile



def add_username(username):
    user = Profile(username=username)
    user.save()

def get_username_info(username):
    info = Profile.objects.filter(username=username)
    return info.values()

def add_tree_to_profile(trees, username):
    user = get_username_info(username)
    temp_user = user[0]


    for obj in trees:
        if obj['id'] not in temp_user['subscribedTrees'].split(','):
            if temp_user['subscribedTrees'] == '':
                temp = '' + str(obj['id'])

            else:
                print(abd)
                temp = temp_user['subscribedTrees'] + "," + obj['id']
            try:
                user[0]['subscribedTrees'] = temp
                print(abd)
                user.save()
            except TypeError as e:
                pass


    return True