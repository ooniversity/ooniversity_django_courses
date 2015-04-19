from django.conf.urls import patterns, include, url
from django.contrib import admin
from courses.views import *

urlpatterns = patterns('',

    url(r'^(?P<course_id>\d+)/$', course_detail, name='course'),
    url(r'^\d*/$', course_detail, name='course_detail'),

)
