from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<course_id>\d+)/$', views.course_detail, name='detail'),
    url(r'^add_course/$', views.add_course, name='add_course'),
    url(r'^edit_course/(?P<pk>\d+)/$', views.edit_course, name='edit_course'),
    url(r'^delete_course/(?P<pk>\d+)/$', views.delete_course, name='delete_course'),
)
