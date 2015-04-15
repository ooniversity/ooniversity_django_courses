from django.conf.urls import include, url, patterns
from django.contrib import admin
from pybursa import views

urlpatterns =  patterns('',
    # Examples:
    url(r'^$', views.show_index, name='index_pybursa'),
    url(r'^contacts/', views.contacts, name='contacts_pybursa'),
    url(r'^students', include('students.urls', namespace = "students")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^quadratic/', include('quadratic.urls', namespace = "quadratic")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^courses/(?P<id>\d+)/$', views.show_course, name = 'course'),
    url(r'^coaches/(?P<id>\d+)/$', views.show_coach, name = 'coach'),
)
