from django.http import HttpResponse
from django.conf.urls import patterns, include, url
from quadratic.views import quadratic_results

urlpatterns = patterns('',
                       url(r'^results/$', quadratic_results),
                       )
