from django.conf.urls import patterns, url
from views import results

urlpatterns = patterns('',
    url(r'^results/$', results, name='results'),
)
