from django.conf.urls import patterns, include, url
from courses.views import add_lesson, CourseDetailView, CourseCreateView, CourseUpdateView, CourseDeleteView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', CourseDetailView.as_view(), name='course_description'),
    url(r'^add/$', CourseCreateView.as_view(), name='add_course'),
    url(r'^edit/(?P<pk>\d+)/$', CourseUpdateView.as_view(), name='edit_course'),
    url(r'^delete/(?P<pk>\d+)/$', CourseDeleteView.as_view(), name='delete_course'),
    url(r'^(?P<course_id>\d+)/add_lesson/$', add_lesson, name='add_lesson'),
]