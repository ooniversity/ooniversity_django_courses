from django.conf.urls import patterns, url

from students.views import StudentListView, StudentDetailView
from students.views import StudentCreateView, StudentUpdateView, StudentDeleteView


urlpatterns = patterns('',

    url(r'^students/$', StudentListView.as_view(), name = 'student-list'),
    url(r'^students/(?P<pk>\d+)/$', StudentDetailView.as_view(), name = 'student-info'),

    # URLs for edition students
    url(r'^students/add/$', StudentCreateView.as_view(), name='student-add'),
    url(r'^students/edit/(?P<pk>\d+)/$', StudentUpdateView.as_view(), name='student-edit'),
    url(r'^students/remove/(?P<pk>\d+)/$', StudentDeleteView.as_view(), name='student-del'),

)
