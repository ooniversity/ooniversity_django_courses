from django.conf.urls import patterns, url
from django.contrib import admin
from django.shortcuts import render
from students import views

urlpatterns = patterns('',
                       url(r'^$', views.students_list, name="students_list"),
                       url(r'^(?P<id>\d+)/$', views.student_info,
                           name="student_detail"),
                       url(r'^add/$', views.student_adding,
                           name="student_add"),
                       url(r'^edit_student/(?P<pk>\d+)/$', views.edit_student,
                           name="edit_student"),
                       url(r'^delete_student/(?P<pk>\d+)/$', views.delete_student,
                           name="delete_student"),
                       )
