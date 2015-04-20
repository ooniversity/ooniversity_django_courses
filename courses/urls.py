from django.conf.urls import patterns, include, url
from django.contrib import admin
from courses.views import *

urlpatterns = patterns('',

    url(r'^(?P<course_id>\d+)/$', course_detail, name='course'),
    url(r'^add/$', course_add, name='course_add'),
    url(r'^edit/(?P<course_id>\d+)/$', course_edit, name='course_edit'),
    url(r'^delete/(?P<course_id>\d+)/$', course_delete, name='course_delete'),
    #url(r'^\d*/$', course_detail, name='course_detail'),
    url(r'^(?P<course_id>\d+)/add_lesson/$', lesson_add, name='lesson_add'),

)
