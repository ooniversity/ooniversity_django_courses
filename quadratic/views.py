from django.shortcuts import render
from django.http import HttpResponse


def results(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    return HttpResponse ("a = {0}, b = {1}, c = {2}".format(a, b, c))
