from django.conf.urls import patterns, include, url

from students.views import students_list, student_detail, student_add

urlpatterns = patterns(
    '',
    url(r'^$', students_list, name='students-list'),
    url(r'^(?P<pk>\d+)/$', student_detail, name='student-detail'),
    url(r'^add/$', student_add, name="student-add"),
)
