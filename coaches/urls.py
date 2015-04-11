from django.conf.urls import patterns, url

from coaches.views import *

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', coach, name='coach'),
)