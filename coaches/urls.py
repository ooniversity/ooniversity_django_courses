from django.conf.urls import patterns, url

from coaches import views

urlpatterns = patterns('coaches.views',
    url(r'^/(?P<coach_id>\d+)/$', views.coach_d, name='coach_d'), 
)
