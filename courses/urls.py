from django.conf.urls import patterns, url
from courses.views import CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView, lesson_add


urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', CourseDetailView.as_view(), name='course_detail'),
    url(r'^add/$', CourseCreateView.as_view(), name='course_add'),
    url(r'^edit/(?P<pk>\d+)/$', CourseUpdateView.as_view(), name='course_edit'),
    url(r'^remove/(?P<pk>\d+)/$', CourseDeleteView.as_view(), name='course_remove'),
    url(r'^(?P<course_id>\d+)/add_lesson/$', lesson_add, name='lesson_add'),
)
