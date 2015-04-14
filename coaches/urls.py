from django.conf.urls import patterns, include, url
from coaches.models import Coach
from coaches.views import allcoaches, onecoach

urlpatterns = patterns('',
    url(r'^$', allcoaches, name="index"),
    url(r'^(?P<pk>\d+)/$', onecoach, name='oneof'),
)