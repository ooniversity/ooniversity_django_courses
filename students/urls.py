from django.conf.urls import patterns, include, url
from django.contrib import admin

from students.views import *

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', StudentsView.as_view(), name='students'),
    url(r'^(?P<id>\d+)/$', StudentView.as_view(), name='student'),
)
