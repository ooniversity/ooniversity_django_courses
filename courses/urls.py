from django.conf.urls import patterns, url

from courses.views import course_coaches


urlpatterns = patterns('',

    url(r'^courses/(?P<id_course>\d+)/$', course_coaches, name = 'course-coaches'),

)
