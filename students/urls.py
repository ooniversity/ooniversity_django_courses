from django.conf.urls import patterns, url
from django.contrib import admin
from django.shortcuts import render
from students import views

urlpatterns = patterns('',
                       url(r'^$', views.StudentsListView.as_view(), name="student_list"),
                       url(r'^(?P<pk>\d+)/$', views.StudentDetailView.as_view(),
                           name="student_detail"),
                       url(r'^add/$', views.StudentCreateView.as_view(),
                           name="student_add"),
                       url(r'^edit_student/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(),
                           name="edit_student"),
                       url(r'^delete_student/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(),
                           name="delete_student"),
                       )
