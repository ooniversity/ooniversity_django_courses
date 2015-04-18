# coding=utf-8
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse

from Quadratic import quadratic_eval
from QuadraticForm import QuadraticForm


def index(request):
    return HttpResponse('index.html')

def results(request):
    variables = {}

    if request.method == 'GET' and len(request.GET) > 0:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            variables = quadratic_eval(**form.cleaned_data)

    else:
        form = QuadraticForm()
    
    return render(request, 'quadratic/quadratic_results.html', {
        'variables':variables,
        'form': form, })

