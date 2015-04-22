from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',
	url(r'^$', views.StudentListView.as_view(), name='students_all'),
    url(r'^(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name='student_info'),
    url(r'^add/$', views.StudentCreateView.as_view(), name='student_add'),
    url(r'^edit/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(), name='student_edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(), name='student_remove'),
)