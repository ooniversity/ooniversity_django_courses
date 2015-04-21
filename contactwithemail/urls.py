from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from contactwithemail import views 

urlpatterns = patterns('',
	url(r'^$', views.send_feedback, name='feedback'),
	#url(r'^$', views.EmailCreateView.as_view(), name='feedback'),
	url(r'^success/$', TemplateView.as_view(template_name='contactwithemail/success.html'), name = 'success'),
)