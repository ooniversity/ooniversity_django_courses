from django.conf.urls import url
from . import views
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


urlpatterns = [
    url(r'^$', views.StudentListView.as_view(), name='list-students'), 
    url(r'^(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name='student'),
    url(r'^edit/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(), name='edit_student'),
    url(r'^remove/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(), name='remove_student'),
    url(r'^add/$', views.StudentCreateView.as_view(), name='add_student'),
]

