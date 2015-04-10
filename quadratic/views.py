# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def checktype(var):
    try:
        int(var)
    except ValueError:
       var = [var, 'stringtype']
    return var

def quadratic_results(request):
    dictionary = {'a': '', 'b': '', 'c': '', 'nd': 'коэффициент не определён',
            'ni': 'коэффициент не целое число'}
    for i in dictionary:
        if i in request.GET:
            dictionary[i] = request.GET.get(i)
            if dictionary[i] != '':
                dictionary[i] = checktype(dictionary[i])

    if dictionary['a'] != '0':
        for i in dictionary:
            if dictionary[i] != '' and type(dictionary[i]) is not list:
                pass
            else:
                return render(request, 'quadratic.html', dictionary)
    else:
        return render(request, 'quadratic.html', dictionary)
    discr = float(dictionary['b']) ** 2 - 4 * float(dictionary['a']) * float(dictionary['c'])
    x1 = 0
    x2 = 0
    if discr == 0:
        x1 = x2 = -float(dictionary['b']) / 2*float(dictionary['a'])
    elif discr > 0:
        x1 = (-float(dictionary['b']) + discr ** 0.5) / (2 * float(dictionary['a']))
        x2 = (-float(dictionary['b']) - discr ** 0.5) / (2 * float(dictionary['a']))
    dictionary['discr'] = int(discr)
    dictionary['x1'] = x1
    dictionary['x2'] = x2
    return render(request, 'quadratic.html', dictionary)