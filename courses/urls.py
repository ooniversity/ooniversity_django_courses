from django.conf.urls import patterns, url
from courses.views import courses_home_page, courses_one_of


urlpatterns = patterns('',
    url(r'^$', courses_home_page, name='index'),
    url(r'^(?P<pk>\d+)/$', courses_one_of, name='oneof'),
)