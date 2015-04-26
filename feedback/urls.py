from django.conf.urls import patterns, include, url
from django.contrib import admin
from feedback.views import *

urlpatterns = patterns('',

    url(r'^$', FeedbackView.as_view(), name='feedback'),
    #url(r'^$', feedback, name='feedback'),
)
