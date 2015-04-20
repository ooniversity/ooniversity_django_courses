from django.conf.urls import patterns, include, url
from courses.views import *

urlpatterns = [
    url(r'^(?P<course_id>\d+)/$', course_description, name='course_description'),
    url(r'^add/$', add_course, name='add_course'),
    url(r'^edit/(?P<course_id>\d+)/$', edit_course, name='edit_course'),
    url(r'^delete/(?P<course_id>\d+)/$', delete_course, name='delete_course'),
    url(r'^(?P<course_id>\d+)/add_lesson/$', add_lesson, name='add_lesson'),
]