from django.conf.urls import patterns, url

from courses.views import course_coaches
from courses.views import add_course, edit_course, delete_course
from courses.views import add_lesson


urlpatterns = patterns('',

    url(r'^courses/(?P<id_course>\d+)/$', course_coaches, name='course-coaches'),


    # URLs for edition courses
    url(r'^courses/add/$', add_course, name='add-course'),
    url(r'^courses/edit/(?P<pk_course>\d+)/$', edit_course, name='edit-course'),
    url(r'^courses/remove/(?P<pk_course>\d+)/$', delete_course, name='del-course'),

    # URLs for edition lessons
    url(r'^courses/(?P<pk_course>\d+)/add_lesson/$', add_lesson, name = 'add-lesson'),

)
