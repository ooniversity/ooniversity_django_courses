from django.conf.urls import patterns, include, url
from students.views import students, students_details

urlpatterns = patterns('',
    url(r'^$', students, name='students_list'),
    url(r'^(?P<pk>\d+)/$', students_details, name='student_details'),
)