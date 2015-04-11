from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<coach_id>\d+)/$', views.coach, name='coach'),
]