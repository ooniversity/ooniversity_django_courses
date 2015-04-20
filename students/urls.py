from django.conf.urls import patterns, url
from students.views import StudentsListView, student_detail, student_add, student_edit, student_remove


urlpatterns = patterns('',
    url(r'^$', StudentsListView.as_view(), name='student_list'),
    url(r'^(?P<student_id>\d+)/$', student_detail, name='student_detail'),
    url(r'^add/$', student_add, name='student_add'),
    url(r'^edit/(?P<student_id>\d+)/$', student_edit, name='student_edit'),
    url(r'^remove/(?P<student_id>\d+)/$', student_remove, name='student_remove'),
)
