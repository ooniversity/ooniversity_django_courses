from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa.views import contact, student_l
from quadratic import views
from courses import views
#from students import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^index/$', views.IndexView.as_view(), name='index'),

    url(r'^contact/$', contact, name ='contact'),
    #url(r'^student_list/$', student_l, name='student_l'),
    #url(r'^student_detail/$', student_d, name = 'student_d'),

    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^admin/', include(admin.site.urls)),
)
