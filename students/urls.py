from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.list_students, name='list-students'), 
    url(r'^(?P<student_id>\d+)/$', views.student, name='student'),
    url(r'^edit/(?P<student_id>\d+)/$', views.edit_student, name='edit_student'),
    url(r'^remove/(?P<student_id>\d+)/$', views.remove_student, name='remove_student'),
    url(r'^add/$', views.add_student, name='add_student'),
]

