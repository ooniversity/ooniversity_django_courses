from django.conf.urls import patterns, include, url
from students.views import *

urlpatterns = [
    url(r'^$', StudentListView.as_view(), name='students_of_the_course'),
    url(r'^(?P<pk>\d+)/$', StudentDetailView.as_view(), name='student_info'),
    url(r'^add/$', StudentCreateView.as_view(), name='add_student'),
    url(r'^edit/(?P<pk>\d+)/$', StudentUpdateView.as_view(), name='edit_student'),
    url(r'^delete/(?P<pk>\d+)/$', StudentDeleteView.as_view(), name='delete_student'),
]

