from django.conf.urls import patterns, url
from views import coach_detail

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', coach_detail, name="coach_detail"),
)
