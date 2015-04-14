# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',


    url(r'^$', views.show_students, name = 'student_list'),
    url(r'^(?P<id>\d+)/$', views.show_student_detail, name = 'student_detail'),
)

