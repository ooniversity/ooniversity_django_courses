from django.conf.urls import patterns, include, url

from students import views

urlpatterns = patterns(
    '',
    url(r'^$', views.StudentListView.as_view(), name='students-list'),
    url(r'^(?P<pk>\d+)/$', views.StudentDetailView.as_view(),
        name='student-detail'),
    url(r'^add/$', views.StudentCreateView.as_view(), name="student-add"),
    url(r'^edit/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(),
        name="student-edit"),
    url(r'^remove/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(),
        name="student-delete"),
)
