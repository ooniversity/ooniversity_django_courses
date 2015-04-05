from django.conf.urls import patterns, url

from quadratic.views import quadratic_results

urlpatterns = patterns('',
    url(r'^results/$', quadratic_results, name='index'),
)
