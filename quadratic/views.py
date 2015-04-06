# coding=utf-8
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse

from Quadratic import Quadratic

def index(request):
    return HttpResponse('index.html')

def results(request):
    errors = {}

    a = request.GET.__getitem__('a')
    b = request.GET.__getitem__('b')
    c = request.GET.__getitem__('c')

    variables = request.GET.dict()
    for var in variables:
        if variables[var] == "":
            errors[var] = 'коэффициент не определен'
        if variables[var].isalpha():
            errors[var] = 'коэффициент не целое число'

    if variables['a'].isdigit() and int(variables['a']) == 0:
        errors['a'] = 'коэффициент при первом слагаемом не может быть равен нулю'

    if len(errors)==0:
        quad = Quadratic(int(a), int(b), int(c))
        quad.calc_discrim()
        d = quad.get_discrim()
        variables.update(d=d)

        if d >= 0:
            x1 = quad.get_eq_root()
            x2 = quad.get_eq_root(order=2)
            variables.update(x1=x1, x2=x2)
    
    return render(request, 'quadratic/quadratic_results.html', {'variables':variables, 'errors':errors})

