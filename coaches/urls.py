from django.conf.urls import patterns, include, url

from coaches.views import coach_show

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', coach_show, name='coach_show'),
)
