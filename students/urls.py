from django.conf.urls import patterns, include, url
from students import views

urlpatterns = patterns('',
    url(r'^$', views.StudentsList.as_view(), name='students_list'),
    url(r'^(?P<pk>\d+)/$', views.StudentDetails.as_view(),
        name='student_details'),
    url(r'^add/$', views.StudentAdd.as_view(), name="student_add"),
    url(r'^edit/(?P<pk>\d+)/$', views.StudentUpdate.as_view(),
        name="student_edit"),
    url(r'^remove/(?P<pk>\d+)/$', views.StudentDelete.as_view(),
        name="student_remove"),
)