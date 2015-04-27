from django.conf.urls import patterns, include, url
from django.contrib import admin

from students.views import *

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', StudentsView.as_view(), name='students'),
    url(r'^(?P<pk>\d+)/$', StudentView.as_view(), name='student'),
    url(r'^add/$', StudentCreateView.as_view(), name='student_add'),
    url(r'^edit/(?P<pk>\d+)/$', StudentUpdateView.as_view(), name='student_edit'),
    url(r'^remove/(?P<pk>\d+)/$', StudentDeleteView.as_view(), name='student_remove'),
)
