from django.conf.urls import patterns, url

from views import *


urlpatterns = patterns('',
	url(r'^$', LetterCreateView.as_view(), name='letter'),	
	)
