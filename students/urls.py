from django.conf.urls import patterns, include, url
from django.contrib import admin
#from students import views
from students.views import *

urlpatterns = patterns('',

    url(r'^(?P<student_id>\d+)/$', student_one, name='student_one'),
    url(r'^\d*$', students, name='students'),
    url(r'^add/$', student_add, name='student_add'),
    url(r'^edit/(?P<stud_id>\d+)/$', student_edit, name='student_edit'),
    url(r'^remove/(?P<stud_id>\d+)/$', student_delete, name='student_delete'),
)
