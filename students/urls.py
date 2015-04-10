from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.list_students, name='list-students'), 
    url(r'^(?P<student_id>\d+)/$', views.student, name='student'),
]

