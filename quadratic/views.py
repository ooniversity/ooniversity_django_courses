# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse

def checktype(var):
    try:
        int(var)
    except ValueError:
       var = [var, 'stringtype']
    return var

def quadratic_results(request):
    dict = {'a': '', 'b': '', 'c': '', 'nd': 'коэффициент не определён',
            'ni':'коэффициент не целое число'}
    for i in dict:
        if i in request.GET:
            dict[i] = request.GET[i]
            if dict[i] != '':
                dict[i] = checktype(dict[i])

    if dict['a'] != '0':
        for i in dict:
            if dict[i] != '' and type(dict[i]) is not list:
                pass
            else:
                return render(request, 'quadratic.html', dict)
    else:
        return render(request, 'quadratic.html', dict)
    discr = float(dict['b']) ** 2 - 4 * float(dict['a']) * float(dict['c'])
    x1 = 0
    x2 = 0
    if discr == 0:
        x1 = x2 = -float(dict['b']) / 2*float(dict['a'])
    elif discr > 0:
        x1 = (-float(dict['b']) + discr ** 0.5) / (2 * float(dict['a']))
        x2 = (-float(dict['b']) - discr ** 0.5) / (2 * float(dict['a']))
    dict['discr'] = int(discr)
    dict['x1'] = x1
    dict['x2'] = x2
    return render(request, 'quadratic.html', dict)