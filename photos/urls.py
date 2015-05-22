# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from photos import views


urlpatterns = patterns('',

    url(r'^$', views.PhotoListView.as_view(), name = 'photo-list'),
    url(r'^(?P<pk>\d+)/$', views.PhotoDetailView.as_view(), name = 'photo-detail'),
)
