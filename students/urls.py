from django.conf.urls import patterns, url
from students import views

urlpatterns = patterns('',
    url(r'^$', views.StudentListView.as_view(), name='students'),
    url(r'^(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name='get_student'),
    url(r'^add/$', views.StudentCreateView.as_view(), name='add_student'),
    url(r'^edit/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(), name='edit_student'),
    url(r'^remove/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(), name='remove_student'),
)
