from django.conf.urls import patterns, include, url

from courses import views


urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name='show'),
    url(r'^(?P<course_id>\d+)/add_lesson/$', views.lesson_add,
        name="lesson-add"),
    url(r'^edit_lesson/(?P<pk>\d+)/$', views.lesson_edit, name="lesson-edit"),
    url(r'^delete_lesson/(?P<pk>\d+)/$', views.lesson_delete,
        name="lesson-delete"),
    url(r'^add/$', views.CourseCreateView.as_view(), name="course-add"),
    url(r'^edit/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(),
        name="course-edit"),
    url(r'^remove/(?P<pk>\d+)/$', views.CourseDeleteView.as_view(),
        name="course-delete"),

)
