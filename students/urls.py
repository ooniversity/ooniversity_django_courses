from django.conf.urls import url, patterns
from students import views

urlpatterns =  patterns('',
    url(r'^/$', views.show_students, name='student_list'),
    url(r'^/(?P<id>\d+)/$', views.show_student, name = 'student_detail'),
    url(r'^/add/$', views.add_student, name='add_student'),
    url(r'^/edit/(?P<id>\d+)/$', views.edit_student, name='add_student'),
    url(r'^/delete/(?P<id>\d+)/$', views.delete_student, name='delete_student'),
)
