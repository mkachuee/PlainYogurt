from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length=200)     # username link between User model and Profile model
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)

FAKE_PROFILE = Profile()
FAKE_PROFILE.username = "xyz1"
FAKE_PROFILE.firstName = "Sajad"
FAKE_PROFILE.lastName = "Darabi"