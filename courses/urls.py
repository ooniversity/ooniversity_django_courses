# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns('',

    url(r'^(?P<id>\d+)/$', views.show_courses, name = 'courses'),
)

