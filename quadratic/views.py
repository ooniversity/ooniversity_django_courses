# -*- coding: utf-8 -*-

from django.shortcuts import render

def quadratic_results(request):
    a = None
    b = None
    c = None

    a = check_in_reques('a', request)
    b = check_in_reques('b', request)
    c = check_in_reques('c', request)
    a = check_is_digit(a, True)
    b = check_is_digit(b)
    c = check_is_digit(c)

    discriminant = None
    root_message = ''

    if isinstance(a, int) and isinstance(b, int) and isinstance(c, int):
        discriminant = b*b - 4 * a * c
        print discriminant, int(discriminant) == 0
        if discriminant < 0:
            root_message = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
        elif int(discriminant) == 0:
            print 'd = 0'
            x = -b / 2 * a
            root_message = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {0:.1f}'.format(x)
        else:
            x1 = (-b + discriminant ** (1.0/2))/ 2 * a
            x2 = (-b - discriminant ** (1.0/2))/ 2 * a
            root_message = 'Квадратное уравнение имеет два действительных корня: x1 = {0:.1f}, x2 = {1:.1f}'.format(x1,x2)

    return render(request, 'quadratic/result.html', {
            'a': a,'b': b,'c': c, 'discriminant':discriminant,
            'root_message':root_message
        })

def check_in_reques(param, request):
    value = None
    if param not in request.GET:
        value = 'коэффициент не найден!'
    elif not request.GET[param]:
        value = 'коэффициент не определен!'
    else: value = request.GET[param]
    return value
def check_is_digit(value, first_param=False):
    if isinstance(value, str):
        return value
    try:
        int(value)
    except ValueError:
        return 'коэффициент не целое число'
    if value.find('.') >= 0:
        return 'коэффициент не целое число'
    elif first_param and int(value) == 0:
        return 'коэффициент при первом слагаемом уравнения не может быть равен нулю'
    else: value = int(value)
    return value
