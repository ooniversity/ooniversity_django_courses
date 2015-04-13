from django.conf.urls import patterns, url

from views import coach_info


urlpatterns = patterns('',  
	url(r'^(?P<coach_id>\d+)/$', coach_info, name='coach_info'))
