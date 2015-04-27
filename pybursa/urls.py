from django.conf.urls import patterns, include, url
from django.contrib import admin
from students.views import StudentsListView
from feedback import views

urlpatterns = patterns('',
                       url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),
                       url(r'^$', 'courses.views.index', name='home'),
                       url(r'^courses/', include('courses.urls')),
                       url(r'^contact/', 'students.views.contact', name='contact'),
                       url(r'^students/', StudentsListView.as_view(), name='student_list'),
                       url(r'^student_detail/', include('students.urls')),
                       url(r'^coach/', include('coaches.urls')),
                       url(r'^feedback/', views.FeedbackCreateView.as_view(), name='feedback'),

                       url(r'^admin/', include(admin.site.urls)),
                       )
