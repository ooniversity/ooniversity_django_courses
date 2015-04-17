# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from students import views


urlpatterns = patterns('',

    url(r'^$', views.show_students, name = 'student-list'),
    url(r'^(?P<id>\d+)/$', views.show_student_detail, name = 'student-detail'),
    url(r'^add/$', views.create_student, name = 'create-student'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit_student, name = 'edit-student'),
    url(r'^remove/(?P<pk>\d+)/$', views.remove_student, name = 'remove-student'),

)

