from django.conf.urls import patterns, include, url

from students.views import (
    students_list, student_detail, student_add, student_edit, student_delete)

urlpatterns = patterns(
    '',
    url(r'^$', students_list, name='students-list'),
    url(r'^(?P<pk>\d+)/$', student_detail, name='student-detail'),
    url(r'^add/$', student_add, name="student-add"),
    url(r'^edit/(?P<pk>\d+)/$', student_edit, name="student-edit"),
    url(r'^remove/(?P<pk>\d+)/$', student_delete, name="student-delete"),
)
