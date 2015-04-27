from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns(
    '',
    url(r'^$', views.CourseView.as_view(), name='courses'),
    url(r'^(?P<pk>\d+)/$', views.CourseDetialView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/add_lesson/$', views.LessonCreateView.as_view(), name='add_lesson'),
    url(r'^(?P<pk>\d+)/edit_lesson/$', views.LessonUpdateView.as_view(), name='edit_lesson'),
    url(r'^(?P<pk>\d+)/remove_lesson/$', views.LessonDeleteView.as_view(), name='remove_lesson'),
    url(r'^add/$', views.CourseCreateView.as_view(), name='course_add'),
    url(r'^edit/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(), name='course_edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.CourseDeleteView.as_view(), name='course_remove'),
)
