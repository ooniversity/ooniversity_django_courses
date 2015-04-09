from django.conf.urls import patterns, url
from courses.views import course_plan

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', course_plan, name='lessons'),
)
