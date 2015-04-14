from django.conf.urls import patterns, include, url
from courses.views import *

urlpatterns = [
    url(r'^(?P<course_id>\d+)/$', course_description, name='course_description'),
]
