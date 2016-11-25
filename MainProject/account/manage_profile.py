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
def find_username_info(username):
    info = Profile.filter(username=username)
    return info.values()
def add_tree_to_profile(trees, username):
    user = find_username_info(username)

    t = False
    for obj in trees:
        for tup in user['subscribedTrees']:
            if (tup['DIRLink'] == obj['DIRLink']):
                t = True
                break

        if t:
            try:
                user.subscribedTrees.add(obj)
                user.save()

            except TypeError as e:
                pass
        else:
            pass

    return True