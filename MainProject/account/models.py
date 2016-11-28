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
    username = models.CharField(max_length=200, primary_key=True)     # username link between User model and Profile model
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    dob = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subscribedTrees = models.CharField(max_length=200)
