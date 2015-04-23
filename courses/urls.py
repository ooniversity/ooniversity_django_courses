from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^(?P<course_id>\d+)/$', views.course_detail, name='detail'),
    url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/add_lesson/$', views.add_lesson, name='add_lesson'),
    # url(r'^add_course/$', views.add_course, name='add_course'),
    # url(r'^edit_course/(?P<pk>\d+)/$', views.edit_course, name='edit_course'),
    # url(r'^delete_course/(?P<pk>\d+)/$', views.delete_course, name='delete_course'),
    url(r'^add_course/$', views.CourseCreateView.as_view(), name='add_course'),
    url(r'^edit_course/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(), name='edit_course'),
    url(r'^delete_course/(?P<pk>\d+)/$', views.CourseDeleteView.as_view(), name='delete_course'),
)
