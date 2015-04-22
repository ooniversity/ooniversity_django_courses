from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',
    # url(r'^$', views.student, name='index'),
    url(r'^$', views.StudentListView.as_view(), name='index'),
    # url(r'^(?P<pk>\d+)/$', views.student_detail, name='detail'),
    url(r'^(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name='detail'),
    # url(r'^add_student/$', views.add_student, name='add_student'),
    url(r'^add_student/$', views.StudentCreateView.as_view(), name='add_student'),
    # url(r'^edit_student/(?P<pk>\d+)/$', views.edit_student, name='edit_student'),
    url(r'^edit_student/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(), name='edit_student'),
    # url(r'^delete_student/(?P<pk>\d+)/$', views.delete_student, name='delete_student'),
    url(r'^delete_student/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(), name='delete_student'),
)
