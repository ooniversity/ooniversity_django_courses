from django.conf.urls import patterns, include, url
from coaches.views import *

urlpatterns = [
    url(r'^(?P<coach_id>\d+)/$', coach_info, name='coach_info'),
]
