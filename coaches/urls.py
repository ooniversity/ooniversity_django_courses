from django.conf.urls import patterns, url
from coaches import views


urlpatterns = patterns('',
   url(r'(?P<coa>\d+)/$', views.coach, name='coach'),

)
