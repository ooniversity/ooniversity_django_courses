from django.conf.urls import patterns, url

from coaches import views

urlpatterns = patterns('',
                       url(r'^(?P<pk>\d+)/$',
                           views.coach_d, name='coach_d'),)
