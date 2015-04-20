from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<course_id>\d+)/$', views.course_description, name='course_description'),
    url(r'^(?P<course_id>\d+)/add_lesson/$', views.add_lesson, name='add_lesson'),    
]