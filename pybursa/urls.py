from django.conf.urls import patterns, include, url
from django.contrib import admin
from pybursa.views import IndexView
from contact.views import ContactFormView
from django.views.generic import TemplateView

urlpatterns = patterns(
    '', url(r'^$', IndexView.as_view(), name='index'),
    url(r'^index/$', IndexView.as_view(), name='index'),
    url(r'^contact_us/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'feedback/$',  ContactFormView.as_view(), name='feedback'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students', include('students.urls', namespace="students")),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
    url(r'^contact/', include('contact.urls', namespace="contacts")),

    url(r'^admin/', include(admin.site.urls)),
)
