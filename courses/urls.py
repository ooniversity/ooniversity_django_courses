from django.conf.urls import patterns, url
from courses import views


urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name='courses'),
    url(r'add/$', views.CourseCreateView.as_view(), name='add_course'),
    url(r'edit/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(),
        name='edit_course'
        ),
    url(r'remove/(?P<pk>\d+)/$', views.CourseDeleteView.as_view(),
        name='remove_course'
        ),
    url(r'(?P<pk>\d+)/add_lesson/$', views.add_lesson, name='add_lesson'),
)
