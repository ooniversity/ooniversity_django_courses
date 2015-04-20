from django.conf.urls import patterns, url

from courses import views
from courses import views_lesson


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^add/', views.course_add, name='add'),
    url(r'^edit/(?P<pk>\d+)/$', views.course_edit, name='edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.course_remove, name='remove'),
    # lessons
    url(r'^(?P<pk>\d+)/add_lesson/', views_lesson.item_add, name='add_lesson'),
)
