from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', views.CoursePlanView.as_view(), name='lessons'),
    url(r'^(?P<course_id>\d+)/add_lesson/$', views.lesson_add, name="lesson_add"),
    url(r'^edit_lesson/(?P<pk>\d+)/$', views.lesson_edit, name="lesson_edit"),
    url(r'^delete_lesson/(?P<pk>\d+)/$', views.lesson_delete, name="lesson_delete"),
    url(r'^add/$', views.CourseCreateView.as_view(), name="course_add"),
    url(r'^edit/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(), name="course_edit"),
    url(r'^remove/(?P<pk>\d+)/$', views.CourseDeleteView.as_view(), name="course_delete"),
)
