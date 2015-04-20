from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns(
    '',
    url(r'^$', views.CourseView.as_view(), name='courses'),
    url(r'^(?P<pk>\d+)/$', views.CourseDetialView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/add_lesson/$', views.add_lesson, name='add_lesson'),
    url(r'^(?P<pk>\d+)/edit_lesson/$', views.edit_lesson, name='edit_lesson'),
    url(r'^(?P<pk>\d+)/remove_lesson/$', views.remove_lesson, name='remove_lesson'),
    url(r'^add/$', views.course_add, name='course_add'),
    url(r'^edit/(?P<pk>\d+)/$', views.course_edit, name='course_edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.course_remove, name='course_remove'),
)
