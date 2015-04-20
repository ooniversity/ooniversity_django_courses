from django.conf.urls import patterns, include, url
from django.contrib import admin
from coaches.views import *

urlpatterns = patterns('',

    url(r'^(?P<co_id>\d+)/$', coach_detail, name='coach_detail'),
    url(r'^$', coach_detail, name='coach_detail'),
    #url(r'^coaches', coach_detail, {'test':'123234'}, name='coach_detail'),
#http://stackoverflow.com/questions/27219849/django-reverse-with-keyword-arguments-not-found

)
