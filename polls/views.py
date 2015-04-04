from django.shortcuts import render_to_response
#from polls.models import Poll
# Create your views here.
from django.http import HttpResponse


def index(request):
#    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]


    return render_to_response('polls/index.html')

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
