from django.conf.urls import url
from . import views
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name='course_description'),
    url(r'^(?P<pk>\d+)/add_lesson/$', views.LessonsCreateView.as_view(), name='add_lesson'),
    url(r'^(?P<pk>\d+)/edit_lesson/$', views.LessonsUpdateView.as_view(), name='edit_lesson'),
    url(r'^(?P<pk>\d+)/delete_lesson/$', views.LessonsDeleteView.as_view(), name='delete_lesson'),    
]