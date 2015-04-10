from django.conf.urls import patterns, url
from courses.views import course_detail


urlpatterns = patterns('',
    url(r'^(?P<course_id>\d+)/$', course_detail, name='course_detail'),
)
