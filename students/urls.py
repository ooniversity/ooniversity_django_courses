from django.conf.urls import patterns, include, url
from students.views import *

urlpatterns = patterns('',
    url(r'^$', students, name='students_list'),
    url(r'^(?P<pk>\d+)/$', students_details, name='student_details'),
    url(r'^add/$', student_add, name='student_add'),
    url(r'^edit/(?P<_id>\d+)/$', student_edit, name='student_edit'),
    url(r'^remove/(?P<id>\d+)/$', student_delete, name='student_remove'),
)