from django.conf.urls import patterns, url
from coaches import views

urlpatterns = patterns('',
    url(r'^(?P<param>\d+)/$', views.coach, name='coach'),
)
