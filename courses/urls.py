from django.conf.urls import patterns, include, url

from courses.views import (
    course_show, course_delete, course_edit, course_add,
    lesson_edit, lesson_delete, lesson_add)

urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', course_show, name='show'),
    url(r'^(?P<course_id>\d+)/add_lesson/$', lesson_add, name="lesson-add"),
    url(r'^edit_lesson/(?P<pk>\d+)/$', lesson_edit, name="lesson-edit"),
    url(r'^delete_lesson/(?P<pk>\d+)/$', lesson_delete, name="lesson-delete"),
    url(r'^add/$', course_add, name="course-add"),
    url(r'^edit/(?P<pk>\d+)/$', course_edit, name="course-edit"),
    url(r'^remove/(?P<pk>\d+)/$', course_delete, name="course-delete"),

)
