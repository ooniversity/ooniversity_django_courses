from django.conf.urls import patterns, url
from courses import views


urlpatterns = patterns('',
   url(r'(?P<c_id>\d+)/$', views.course, name='courses'),

)
