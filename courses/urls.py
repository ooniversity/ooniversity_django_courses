from django.conf.urls import patterns, url

from views import *


urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', course_info, name='course_info'),
    url(r'^(?P<pk>\d+)/add/', add_lesson, name='add_lesson'),
    url(r'^add/$', add_course, name='add_course'),
    url(r'^edit/(?P<pk>\d+)/$', edit_course, name='edit_course'),
    url(r'^remove/(?P<pk>\d+)/$', remove_course, name='remove_course'),
    )
