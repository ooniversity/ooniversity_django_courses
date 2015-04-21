from django.conf.urls import patterns, include, url
from django.contrib import admin
from quadratic.views import quadratic_results
from pybursa.views import *
from pybursa import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='home'),
    url(r'^polls/', include('courses.urls')),
    url(r'^contact/$', TemplateView.as_view(template_name = 'contact.html'), name = 'contact'),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^quadratic/results', 'quadratic.views.quadratic_results', name = 'quadratic'),
    url(r'^quadratic/', 'quadratic.views.quadratic_start', name = 'quadraticStart'),
    url(r'^admin/', include(admin.site.urls)),
)
