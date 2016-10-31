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

    def testIfDatabaseWriteCorrectly(self):
        s = Subjects(Categories='C', Subjects='S');
        s.save();
        self.assertIs(s.Categories,'C');
        self.assertIs(s.Subjects, 'S');

