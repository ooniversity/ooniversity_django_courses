from django.shortcuts import render
from django.http import HttpResponse

def quadratic_results(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    return HttpResponse('Parameters: %w' % a )