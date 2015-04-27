from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    #url(r'^(?P<pk>\d+)/$', views.CourseDetialView.as_view(), name='detail'),
    url(r'^(?P<question_id>\d+)/add_lesson/$', views.add_lesson_to_course, name='add_lesson'),
    url(r'^(?P<question_id>\d+)/edit_lesson/$', views.edit_lesson_in_course, name='edit_lesson'),
    url(r'^(?P<question_id>\d+)/delete_lesson/$', views.delete_lesson_from_course, name='delete_lesson'),
)
