from django.conf.urls import patterns, include, url
from django.contrib import admin

from pybursa import views
from postman.views import FeedbackView 


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', views.index, name='index'),
    url(r'^$', include('courses.urls', namespace="courses_i")),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
    url(r'^contact/', 'courses.views.contact', name='contact'),
    #url(r'^feedback/', 'postman.views.feedback', name='feedback'),
    url(r'^feedback/', FeedbackView.as_view(), name='feedback'),

    #url(r'^contact/', views.contact, name='contact'),
    url(r'^student_list/', views.student_list, name='student_list'),
    url(r'^student_detail/', views.student_detail, name='student_detail'),

    url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),

    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
