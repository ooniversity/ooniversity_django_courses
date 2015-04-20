from django.conf.urls import patterns, url
from students.views import StudentsListView, StudentDetailView, StudentCreateView, StudentUpdateView, student_remove


urlpatterns = patterns('',
    url(r'^$', StudentsListView.as_view(), name='student_list'),
    url(r'^(?P<pk>\d+)/$', StudentDetailView.as_view(), name='student_detail'),
    url(r'^add/$', StudentCreateView.as_view(), name='student_add'),
    url(r'^edit/(?P<pk>\d+)/$', StudentUpdateView.as_view(), name='student_edit'),
    url(r'^remove/(?P<student_id>\d+)/$', student_remove, name='student_remove'),
)
