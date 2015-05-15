# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from news import views


urlpatterns = patterns('',

    url(r'^$', views.NewListView.as_view(), name = 'new-list'),
    url(r'^(?P<pk>\d+)/$', views.NewDetailView.as_view(), name = 'new-detail'),
)
