from django.conf.urls import patterns, include, url
from django.contrib import admin
from students import views
import courses

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^polls/', include('polls.urls', namespace="polls")),
    # url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),
    # url(r'^courses/', include('courses.urls')),
    
    url(r'^$', 'courses.views.index'),
    url(r'^contact/', 'views.contact', name='contact'),
    url(r'^student_list/', 'views.student_list', name='student_list'),
    url(r'^student_detail/', 'views.student_detail'),
    
    url(r'^admin/', include(admin.site.urls)),
)
