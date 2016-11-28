from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.allSubjects, name='allSubjects'),
    url(r'^(?P<subjectName>[a-z A-Z 0-9 _ -]+)/$', views.specificSubject, name='specificSubject'),
]
