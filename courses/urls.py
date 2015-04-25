from django.conf.urls import patterns, include, url
from courses.views import  CourseEdit, CourseDelete

urlpatterns = patterns('courses.views',
    url(r'^lesson_add/(?P<course_id>\d+)/$', 'lesson_add', name='lesson_add'),
    url(r'^lesson/add/(?P<lesson_id>\d+)/$', 'lesson_add_redirect', name='lesson_add_redirect'),
    url(r'^lesson_mod/(?P<lesson_id>\d+)/$', 'lesson_mod', name='lesson_mod'),
    url(r'^lesson_rem/(?P<lesson_id>\d+)/$', 'lesson_rem', name='lesson_rem'),
    url(r'^lesson/mod/(?P<course_id>\d+)/(?P<lesson_id>\d+)/$', 'lesson_mod_redirect', name='lesson_mod_redirect'),
    url(r'^lesson/rem/(?P<lesson_id>\d+)/$', 'lesson_add_redirect', name='lesson_add_redirect'),

    url(r'^course_mod/(?P<pk>\d+)/$', CourseEdit.as_view(), name='course_mod'),
    url(r'^course_rem/(?P<pk>\d+)/$', CourseDelete.as_view(), name='course_rem'),
    url(r'^course/mod/(?P<course_id>\d+)/$', 'course_mod_redirect', name='course_mod_redirect'),


)
