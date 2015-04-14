from django.conf.urls import patterns, url

from coaches.views import coaches_info

urlpatterns = patterns('',
    url(r'^(?P<coach_id>\d+)/$', coaches_info, name='coaches_info'),
)