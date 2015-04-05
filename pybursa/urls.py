from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render


def index(request):
	return render(request, 'index.html')

def contact(request):
	return render(request, 'contact.html')

def student_list(request):
	return render(request, 'student_list.html')

def student_detail(request):
	return render(request, 'student_detail.html')	

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^student_list/$', student_list, name='stud_list'),
    url(r'^student_detail/$', student_detail, name='stud_detail'),

)