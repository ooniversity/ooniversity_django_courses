#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse

def basic_validation(x):
    if len(x)==0:
        return "коэффициент не определен\n"
    elif x[-1].isdigit() == False:
        return "коэффициент не целое число\n"

def advanced_validation (x):
    if len(x)==0:
        return "коэффициент не определен\n"
    elif x[-1].isdigit() == False:
        return "коэффициент не целое число\n"
    elif int(x)==0:
        return "коэффициент при первом слагаемом не может быть равным нулю \n "

def quadratic_results(request):
    message = ""
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    message += "Квадратное уравнение a*x*x + b*x + c = 0 \n\n"

    message += "a = %s \n" % str(a)
    try:
        message += advanced_validation(a)
    except TypeError:
        pass
    message += "b = %s \n" % str(b)
    try:
        message += basic_validation(b)
    except TypeError:
        pass
    message += "c = %s \n\n" % str(c)
    try:
        message += basic_validation(c)
    except TypeError:
        pass

    if advanced_validation(a) is None and basic_validation(b) is None and basic_validation(c) is None:
        d = float(b)**2-4*float(a)*float(c)
        message += "Дискриминант: d=%d \n\n" % d

        if d < 0:
            message += "Дискриминант меньше нуля, квадратное не имеет действительных решений \n\n"
            #return HttpResponse(message, content_type="text/plain; charset=utf-8")
        elif d == 0:
            x = -float(b) / 2*float(a)
            message += "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1=x2=%0.1f \n\n" % x
            #return HttpResponse(message, content_type="text/plain; charset=utf-8")
        else:
            x1 = (-float(b) + d**(1/2.0))/(2*float(a))
            x2 = (-float(b) - d**(1/2.0))/(2*float(a))
            message += "Квадратное уравнение имеет два действительных корня: x1=%0.1f, x2=%0.1f \n\n" % (x1, x2)
    return HttpResponse(message, content_type="text/plain; charset=utf-8")
