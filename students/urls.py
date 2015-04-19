from django.conf.urls import patterns, url
from students import views


urlpatterns = patterns(
    '', url(r'^/$', views.StudentListView.as_view(), name='students'),
    url(r'^/(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name='student_d'),
    url(r'/add/$', views.create_edit, name='add_student'),
    url(r'/edit/(?P<pk>\d+)/$', views.create_edit, name='edit_student'),
    url(r'/remove/(?P<pk>\d+)/$', views.remove_student, name='remove_student'),
)
