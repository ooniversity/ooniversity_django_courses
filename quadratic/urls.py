from django.conf.urls import patterns, url

from quadratic.views import quadratic_results

urlpatterns = patterns('',
    url(r'^results/(?P<a>\d+)/(?P<b>\d+)/(?P<c>\d+))$', quadratic_results, name='result'),
)