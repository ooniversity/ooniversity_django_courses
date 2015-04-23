from django.conf.urls import url, patterns
from students import views

urlpatterns =  patterns('',
    url(r'^/$', views.StudentListView.as_view(), name='student_list'),
    url(r'^/(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name = 'student_detail'),
    url(r'^/add/$', views.StudentCreateView.as_view(), name='add_student'),
    url(r'^/edit/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(), name='add_student'),
    url(r'^/delete/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(), name='delete_student'),
)
