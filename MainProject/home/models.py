from django.db import models


# Create your models here.
class Subjects(models.Model):
    category = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)

    def __str__(self):
        return self.category + " | " + self.subject + " | " + self.topic


class TreeInfo(models.Model):
    name = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    DIRLink = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " | " + self.category + " | " + self.subject
