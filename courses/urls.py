from django.conf.urls import patterns, url
from courses import views

urlpatterns = patterns('',
                       url(r'^(?P<pk>\d+)/$', views.CoursesDetailView.as_view(), name='course'),
                       url(r'^(?P<pk>\d+)/add_lesson/$', views.add_lesson, name='add_lesson'),
                       url(r'^add/$', views.CoursesCreateView.as_view(), name='course_add'),
                       url(r'^edit/(?P<pk>\d+)/$', views.CoursesUpdateView.as_view(), name='course_edit'),
                       url(r'^delete/(?P<pk>\d+)/$', views.CoursesDeleteView.as_view(), name='course_delete'),
                       )
