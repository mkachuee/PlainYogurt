import os
import sys
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if path not in sys.path:
    sys.path.append(path)
from home.models import TreeInfo
from models import Profile



def add_username(username):
    user = Profile(username=username)
    user.save()
def find_username_info(username):
    info = Profile.filter(username=username)
    return info.values()
def add_tree_to_profile(tree, username):
    user = find_username_info(username)

    t = False
    for tup in user['subscribedTrees']:
        if (tup['DIRLink'] == tree['DIRLink']):
            t = True
            break

    if t:
        try:
            user.subscribedTrees.add(tree)
            user.save()

        except TypeError as e:
            return None
    else:
        return None

    return True