from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',
	url(r'^$', views.StudentListView.as_view(), name='list'),
	url(r'^(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name='detail'),
	#url(r'^$', views.IndexView.as_view(), name='list'),
	#url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
)