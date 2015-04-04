#from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response
#from pybursa_app.models import Student

from django.http import HttpResponse


def index(request):
#    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]


    return render_to_response('index.html')

def contacts(request):
#    return HttpResponse("You're looking at poll %s." % poll_id)
    return render_to_response('contacts.html')

def student_list(request):
#    return HttpResponse("You're looking at the results of poll %s." % poll_id)
    return render_to_response('student_list.html')


def student_detail(request):
#    return HttpResponse("You're voting on poll %s." % poll_id)
    return render_to_response('student_detail.html')
