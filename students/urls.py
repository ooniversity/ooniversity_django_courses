from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from students import views

urlpatterns = patterns('',
    url(r'^$', views.StudentListView.as_view(), name='index'),
    url(r'^add/$', views.StudentCreateView.as_view(), name='add'),
    url(r'^registred/$', TemplateView.as_view(template_name='students/registy_completed.html'), name = 'registred'),
    url(r'^(?P<pk>\d+)/', views.StudentDetailView.as_view(), name='detail'),
    url(r'^edit/(?P<pk>\d+)/', views.StudentUpdateView.as_view(), name='edit'),
    url(r'^delete/(?P<pk>\d+)/', views.StudentDeleteView.as_view(), name='delete'),
)