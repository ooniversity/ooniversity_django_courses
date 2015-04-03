from django.conf.urls import include, url, patterns
from django.contrib import admin
from pybursa import views

urlpatterns =  patterns('',
    # Examples:
    url(r'^$', views.show_index, name='index_pybursa'),
    url(r'^contacts/', views.contacts, name='contacts_pybursa'),
    url(r'^students/', views.students, name='students'),
    url(r'^student_1/', views.student_1, name='student_1'),
    
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
