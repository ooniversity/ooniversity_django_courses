from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<course_id>\d+)/$', views.course_description, name='course-description'),
]