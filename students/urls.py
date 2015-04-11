from django.conf.urls import patterns, include, url

from students.views import students_list, student_detail

urlpatterns = patterns(
    '',
    url(r'^$', students_list, name='students_list'),
    url(r'^(?P<pk>\d+)/$', student_detail, name='student_detail'),
)
