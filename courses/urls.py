from django.conf.urls import patterns, url
from courses.views import *

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', course_plan, name='lessons'),
    url(r'^(?P<course_id>\d+)/add_lesson/$', lesson_add, name="lesson_add"),
    url(r'^edit_lesson/(?P<pk>\d+)/$', lesson_edit, name="lesson_edit"),
    url(r'^delete_lesson/(?P<pk>\d+)/$', lesson_delete, name="lesson_delete"),
    url(r'^add/$', course_add, name="course_add"),
    url(r'^edit/(?P<pk>\d+)/$', course_edit, name="course_edit"),
    url(r'^remove/(?P<pk>\d+)/$', course_delete, name="course_delete"),
)
