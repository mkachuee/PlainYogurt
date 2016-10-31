# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.db import models
from .models import Subjects
from .models import Treeinfo

# Create your tests here.
class SubjectTest(TestCase):
    def trivialTest(self):
        self.assertIs(True, True)

    def testModel(self):
        s = Subjects.objects.create(Categories="C",Subject='S')
        self.assertTrue(isinstance(s,Subjects))
