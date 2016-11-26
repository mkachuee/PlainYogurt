import os
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if path not in sys.path:
    sys.path.append(path)

from django.db import models
from django.contrib.auth.models import User
from home.models import TreeInfo
# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length=200)     # username link between User model and Profile model
    first = models.CharField(max_length=200)
    last = models.CharField(max_length=200)
    subscribedTrees = models.CharField(max_length=200)
