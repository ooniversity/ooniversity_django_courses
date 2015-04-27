from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from courses import views

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name='course_info'),
    url(r'^contacts/$', views.TemplateView.as_view(template_name ='courses/contacts.html'), name='contacts'),
    url(r'^(?P<course_id>\d+)/add_lesson/$', views.add_lesson, name='add_lesson'),
    url(r'^add/$', views.CourseCreateView.as_view(), name='course_add'),
    url(r'^edit/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(), name='course_edit'),
    url(r'^remove/(?P<pk>\d+)/$', views.CourseDeleteView.as_view(), name='course_remove'),
)
