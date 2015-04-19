from django.conf.urls import patterns, url

from students.views import students, student_info


urlpatterns = patterns('',

    url(r'^students/$', students, name = 'student-list'),
    url(r'^students/(?P<id_stud>\d+)/$', student_info, name = 'student-info'),

)
