from django.conf.urls import patterns, url
from coaches.views import coach_info

urlpatterns = patterns('',
    url(r'^coaches/(?P<id_coach>\d+)/$', coach_info, name = 'coach-info'),
)