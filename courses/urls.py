from django.conf.urls import patterns, include, url

from courses.views import course_show, course_delete, course_edit, course_add

urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\d+)/$', course_show, name='show'),
    url(r'^add/$', course_add, name="course-add"),
    url(r'^edit/(?P<pk>\d+)/$', course_edit, name="course-edit"),
    url(r'^remove/(?P<pk>\d+)/$', course_delete, name="course-delete"),

)
