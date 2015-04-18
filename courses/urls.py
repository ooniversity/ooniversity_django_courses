from django.conf.urls import patterns, url
from courses.views import course_detail, course_add, course_edit, course_remove, lesson_add


urlpatterns = patterns('',
    url(r'^(?P<course_id>\d+)/$', course_detail, name='course_detail'),
    url(r'^add/$', course_add, name='course_add'),
    url(r'^edit/(?P<course_id>\d+)/$', course_edit, name='course_edit'),
    url(r'^remove/(?P<course_id>\d+)/$', course_remove, name='course_remove'),
    url(r'^(?P<course_id>\d+)/add_lesson/$', lesson_add, name='lesson_add'),
)
