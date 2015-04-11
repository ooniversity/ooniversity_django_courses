from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa.views import *

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^polls/', include('polls.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),

    url(r'^$', index, name='index'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^student_list/$', student_list, name='student_list'),
    url(r'^student_detail/$', student_detail, name='student_detail'),

    url(r'^quadratic/', include('quadratic.urls')),
   
    url(r'^courses/(?P<course_id>\d+)/$', course_detail, name='course'),
    #url(r'^courses/\d*', course_from_student, name='course_from_student'),
    url(r'^courses/\d*', course_detail, name='course_from_student'),

    url(r'^students/(?P<student_id>\d+)/$', student_one, name='student_one'),
    url(r'^students/\d*$', students, name='students'),
    #url(r'^students/', students, name='students'),
)
