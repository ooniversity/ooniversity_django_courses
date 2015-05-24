# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from courses import views

urlpatterns = patterns('',

    url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name = 'course'),
    #Урлы для редактирование курса
    url(r'^add/$', views.CourseCreateView.as_view(), name = 'create-course'),
    url(r'^edit/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(), name = 'edit-course'),
    url(r'^remove/(?P<pk>\d+)/$', views.CourseDeleteView.as_view(), name = 'remove-course'),
    #Урлы для редактирования урока
    url(r'^(?P<pk>\d+)/add_lesson/$', views.create_lesson, name = 'create-lesson'),
#    url(r'^(?P<pk>\d+)/edit_lesson/$', views.edit_lesson, name = 'edit-lesson'),
#    url(r'^(?P<pk>\d+)/remove_lesson/$', views.remove_lesson, name = 'remove-lesson'),

    #Урлы для редактирования комментариев
    url(r'^(?P<pk>\d+)/add_comment/$', views.CommentCreateView.as_view(), name = 'create-comment'),
    url(r'^(?P<id>\d+)/edit_comment/(?P<pk>\d+)/$', views.CommentUpdateView.as_view(), name = 'edit-comment'),
    url(r'^(?P<id>\d+)/remove_comment/(?P<pk>\d+)/$', views.CommentDeleteView.as_view(), name = 'remove-comment'),

    #Урл для записи на курс
    url(r'^enroll/(?P<pk>\d+)/$', views.MailCourseCreateView.as_view(), name = 'enroll-course'),
)

