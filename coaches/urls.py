from django.conf.urls import patterns, url
from coaches.views import coach_detail


urlpatterns = patterns('',
    url(r'^(?P<coach_id>\d+)/$', coach_detail, name='coach_detail'),
)
