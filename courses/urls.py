from django.conf.urls import patterns, url
from courses.views import courses_home_page, courses_one_of, add_course, edit_course, delete_course, add_lesson


urlpatterns = patterns('',
    url(r'^$', courses_home_page, name='index'),
    url(r'^(?P<pk>\d+)/$', courses_one_of, name='oneof'),
    url(r'^add/$', add_course, name='add'),
    url(r'^edit/(?P<pk>\d+)/$', edit_course, name='edit'),
    url(r'^delete/(?P<pk>\d+)/$', delete_course, name='delete'),
    url(r'^(?P<pk>\d+)/add_lesson/$', add_lesson, name='add_lesson'),
)