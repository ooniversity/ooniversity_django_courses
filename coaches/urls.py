# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from coaches import views

urlpatterns = patterns('',

    url(r'^(?P<id_c>\d+)/$', views.show_coach_detail, name = 'coach_detail'),
)

