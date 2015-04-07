from django.conf.urls import patterns, include, url
from django.contrib import admin
from quadratic.views import *
#from django.http import HttpResponse, HttpResponseNotFound

#def test(request):
#	print "\n--------------------------------------"
#	print request.path
#	print request.method
#	print request.GET, request.POST
#	response = render(request,'test.html')
#	print response.status_code
#	print response['Content-Type']
#	response['Age_MAX!!!'] = 20000
#	return HttpResponseNotFound('DDD!')
#
#def hello(request):
#	return render(request,'index.html')
#	#return HttpResponse('Hello World!')
#
#def hello_python(request):
#	return HttpResponse("Hello Python!")
#
#def sum_two(request, a, b):
#	print a, b
#	d = int(a)+int(b)
#	return HttpResponse('Your result is: % d' % d)



urlpatterns = patterns('',
    url(r'^$', quadratic, name="quadratic"),
    url(r'^result/$', result, name="result"),
    #url(r'^contact/$', contact, name="contact"),
    #url(r'^student_list/$', student_list, name="student_list"),
    #url(r'^student_detail/$', student_detail, name="student_detail"),
    #url(r'^$', index, name="home"),
    #url(r'^instructors/$', 'instructors.views.instructors_list', name="instructors_list"),
    # Examples:
    #url(r'^$', index, name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^python/$', hello_python),
    #url(r'^test/$', test),
    #url(r'^python/(?P<version>2|3)/$', hello_python),
    #url(r'^sum/(?P<a>\d+)/(?P<b>\d+)/$', sum_two),
    #url(r'^admin/', include(admin.site.urls)),
)