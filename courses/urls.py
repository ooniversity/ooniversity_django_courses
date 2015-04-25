from django.conf.urls import patterns, url
from django.contrib import admin
from django.shortcuts import render
from courses import views

urlpatterns = patterns('',
                       url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name="courseinfo"),
                       url(r'^add/', views.CourseCreateView.as_view(), name="add_course"),
                       url(r'^edit_course/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(),
                           name="edit_course"),
                       url(r'^delete_course/(?P<pk>\d+)/$', views.CourseDeleteView.as_view(),
                           name="delete_course"),
                       url(r'^(?P<id>\d+)/add_lesson/$', views.lesson_adding, name="lesson_add"),
                       
                       )
