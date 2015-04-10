from django.conf.urls import patterns, include, url

from courses.views import course_show

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', course_show, name='show'),
)
