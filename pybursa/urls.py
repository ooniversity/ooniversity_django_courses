from django.conf.urls import patterns, include, url
from django.contrib import admin

from pybursa.views import contact, student_l
from quadratic import views
from courses import views

#from quadratic import views


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^index/$', views.IndexView.as_view(), name='index'),
    url(r'^contact/$', contact, name ='contact'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students', include('students.urls', namespace="students")),
    url(r'^coaches', include('coaches.urls', namespace="coaches")),
    url(r'^admin/', include(admin.site.urls))
)
