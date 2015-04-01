from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pybursa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls', namespace = "polls")),
    url(r'^$', views.show_index, name = 'index_itbursa'),
    url(r'^contact/$', views.show_contacts, name = 'contacts_itbursa'),
    url(r'^student_list/$', views.show_students, name = 'student_list'),
    url(r'^student_detail/$', views.show_student_detail, name = 'student_detail'),

    url(r'^admin/', include(admin.site.urls)),

)
