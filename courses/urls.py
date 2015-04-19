from django.conf.urls import patterns, url
from courses.views import course_detail, add_course, edit_course, delete_course

urlpatterns = patterns('',
    url(r'^(?P<course_id>\d+)/$', course_detail, name='course_detail'),
    url(r'^add/$', add_course, name='course-adding'),
    url(r'^edit_course/(?P<pk>\d+)/$', edit_course, name='edit-course'),
    url(r'^delete_course/(?P<pk>\d+)/$', delete_course, name='delete-course'),
)
