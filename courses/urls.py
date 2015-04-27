from django.conf.urls import patterns, include, url
from django.contrib import admin
from courses.views import *

urlpatterns = patterns('',

    #url(r'^(?P<course_id>\d+)/$', course_detail, name='course'),
    #url(r'^add/$', course_add, name='course_add'),
    #url(r'^edit/(?P<pk>\d+)/$', course_edit, name='course_edit'),
    #url(r'^delete/(?P<pk>\d+)/$', course_delete, name='course_delete'),
    url(r'^(?P<pk>\d+)/$', CourseDetailView.as_view(), name='course'),
    url(r'^add/$', CourseCreateView.as_view(), name='course_add'),
    url(r'^edit/(?P<pk>\d+)/$', CourseUpdateView.as_view(), name='course_edit'),
    url(r'^delete/(?P<pk>\d+)/$', CourseDeleteView.as_view(), name='course_delete'),
    #url(r'^\d*/$', course_detail, name='course_detail'),
    url(r'^(?P<pk>\d+)/add_lesson/$', lesson_add, name='lesson_add'),

)
