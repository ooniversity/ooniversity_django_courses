from django.conf.urls import patterns, url

from students.views import students, student_info
from students.views import add_student, edit_student, delete_student


urlpatterns = patterns('',

    url(r'^students/$', students, name = 'student-list'),
    url(r'^students/(?P<id_stud>\d+)/$', student_info, name = 'student-info'),

    # URLs for edition students
    url(r'^students/add/$', add_student, name='student-add'),
    url(r'^students/edit/(?P<pk_stud>\d+)/$', edit_student, name='student-edit'),
    url(r'^students/remove/(?P<pk_stud>\d+)/$', delete_student, name='student-del'),

)
