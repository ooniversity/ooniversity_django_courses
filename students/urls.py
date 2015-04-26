from django.conf.urls import patterns, include, url
from django.contrib import admin
#from students import views
from students.views import *

urlpatterns = patterns('',

    #url(r'^(?P<student_id>\d+)/$', student_one, name='student_one'),#obsolete
    #url(r'^\d*$', students, name='students'), #obsolete
    #url(r'^add/$', student_add, name='student_add'), #obsolete
    #url(r'^edit/(?P<stud_id>\d+)/$', student_edit, name='student_edit'), #obsolete
    #url(r'^remove/(?P<stud_id>\d+)/$', student_delete, name='student_delete'),#obsolete
    url(r'^(?P<pk>\d+)/$', StudentDetailView.as_view(), name='student_one'),
    url(r'^\d*$', StudentListView.as_view(), name='students'),
    url(r'^add/$', StudentCreateView.as_view(), name='student_add'),
    url(r'^edit/(?P<pk>\d+)/$', StudentUpdateView.as_view(), name='student_edit'),
    url(r'^remove/(?P<pk>\d+)/$',  StudentDeleteView.as_view(), name='student_delete'),
    #url(r'^page(?P<page>\d+)/$', PaginatedView.as_view()),
)
