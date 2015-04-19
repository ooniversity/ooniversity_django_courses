from django.conf.urls import patterns, include, url
from django.contrib import admin
from quadratic.views import *

urlpatterns = patterns('',
url(r'^$', quadratic, name="quadratic"),
url(r'^result/$', result, name="result"),
)
