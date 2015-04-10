from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
'''
def index(request):
    t = loader.get_template('index.html')
    c = Context({})
    return HttpResponse(t.render(c))
'''

def contact(request):
    t = loader.get_template('contact.html')
    c = Context({})
    return HttpResponse(t.render(c))

def student_list(request):
    t = loader.get_template('student_list.html')
    c = Context({})
    return HttpResponse(t.render(c))

def student_detail(request):
    t = loader.get_template('student_detail.html')
    c = Context({})
    return HttpResponse(t.render(c))
