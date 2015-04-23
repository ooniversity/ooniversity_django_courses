from django.conf.urls import patterns, include, url
from students import views

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', views.StudentsDetailView.as_view(), name='student_detail'),
    url(r'^add/$', views.StudentsCreateView.as_view(), name='student_add'),
    url(r'^edit/(?P<pk>\d+)/$', views.StudentsUpdateView.as_view(), name='student_edit'),
    url(r'^delete/(?P<pk>\d+)/$', views.StudentsDeleteView.as_view(), name='student_delete'),
)
