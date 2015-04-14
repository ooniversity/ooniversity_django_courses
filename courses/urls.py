from django.conf.urls import patterns, url

from courses.views import course_info

urlpatterns = patterns('',
    url(r'^(?P<course_id>\d+)/$', course_info, name='course_info'),
)