from django.conf.urls import patterns, url
from students.views import *


urlpatterns = patterns('',
    url(r'^$', students_all, name='index'),
    url(r'^(?P<pk>\d+)/$', one_of_student, name='oneof'),
)