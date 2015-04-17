# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from courses import views

urlpatterns = patterns('',

    url(r'^(?P<pk>\d+)/$', views.show_courses, name = 'course'),
    #Урлы для редактирование курса
    url(r'^add/$', views.create_course, name = 'create-course'),
    url(r'^edit/(?P<pk>\d+)/$', views.edit_course, name = 'edit-course'),
    url(r'^remove/(?P<pk>\d+)/$', views.remove_course, name = 'remove-course'),
    #Урлы для редактирования урока
    url(r'^(?P<pk>\d+)/add_lesson/$', views.create_lesson, name = 'create-lesson'),
#    url(r'^(?P<pk>\d+)/edit_lesson/$', views.edit_lesson, name = 'edit-lesson'),
#    url(r'^(?P<pk>\d+)/remove_lesson/$', views.remove_lesson, name = 'remove-lesson'),


)

