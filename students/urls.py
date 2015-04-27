# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from students import views


urlpatterns = patterns('',

    url(r'^$', views.StudentListView.as_view(), name = 'student-list'),
    url(r'^(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name = 'student-detail'),
    url(r'^add/$', views.StudentCreateView.as_view(), name = 'create-student'),
    url(r'^edit/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(), name = 'edit-student'),
    url(r'^remove/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(), name = 'remove-student'),

)

