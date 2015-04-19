from django.conf.urls import patterns, include, url
from quadratic.views import *

urlpatterns = patterns('',
    url(r'^$', quadratic, name='quadratic'),
    url(r'^results/$', results, name='results'),
)
