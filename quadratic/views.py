# -*- coding: utf-8 -*-

from django.shortcuts import render

def quadratic_results(request):
    a = None
    b = None
    c = None

    a_comment = ''
    b_comment = ''
    c_comment = ''

    if 'a' not in request.GET:
        a_comment = 'коэффициент не найден!'
    elif not request.GET['a']:
        a_comment = 'коэффициент не определен!'
    else: a = request.GET['a']
    if 'b' not in request.GET:
        b_comment = 'коэффициент не найден!'
    elif not request.GET['b']:
        b_comment = 'коэффициент не определен!'
    else: b = request.GET['b']
    if 'c' not in request.GET:
        c_comment = 'коэффициент не найден!'
    elif not request.GET['c']:
        c_comment = 'коэффициент не определен!'
    else: c = request.GET['c']

    print a,b,c
    print a_comment, b_comment,c_comment

    try:
        int(a)
    except ValueError:
        if not a_comment:
            a_comment = 'коэффициент не целое число'
    except TypeError:
        print 'a TypeError'
    if a and not a_comment:
        if a.find('.') >= 0:
            a_comment = 'коэффициент не целое число'
        elif int(a) == 0:
            a_comment = 'коэффициент при первом слагаемом уравнения не может быть равен нулю'
        else: a = int(a)

    try:
        int(b)
    except ValueError:
        if not b_comment:
            b_comment = 'коэффициент не целое число'
    except TypeError:
        print 'b TypeError'
    if b and not b_comment:
        if b.find('.') >= 0:
            b_comment = 'коэффициент не целое число'
        else: b = int(b)

    try:
        int(c)
    except ValueError:
        if not c_comment:
            c_comment = 'коэффициент не целое число'
    except TypeError:
        print 'c TypeError'
    if c and not c_comment:
        if c.find('.') >= 0:
            c_comment = 'коэффициент не целое число'
        else: c = int(c)

    discriminant = None
    root_message = ''
    need_show_discriminant = False
    print a_comment, b_comment,c_comment

    if not a_comment and not b_comment and not c_comment:
        print "discr try "
        need_show_discriminant = True
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

    a = none_to_str(a)
    b = none_to_str(b)
    c = none_to_str(c)
    discriminant = none_to_str(discriminant)
    print discriminant
    return render(request, 'quadratic/result.html', {
            'a': a,'b': b,'c': c, 'discriminant':discriminant,
            'root_message':root_message, 'a_comment': a_comment,
            'b_comment': b_comment, 'c_comment': c_comment,
            'need_show_discriminant':need_show_discriminant
        })





"""
def quadratic_results(request):
    a = None
    b = None
    c = None

    a_comment = check_in_reques('a', request)
    b_comment = check_in_reques('b', request)
    c_comment = check_in_reques('c', request)
    if  not a_comment:
        a = request.GET['a']
        a_comment = check_is_digit(a, True)
    if  not b_comment:
        b = request.GET['b']
        b = check_is_digit(b)
    if  not c_comment:
        c = request.GET['c']
        c = check_is_digit(c)

    print a,b,c
    print a_comment,b_comment,c_comment

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

    a_comment = none_to_str(a_comment)
    b_comment = none_to_str(b_comment)
    c_comment = none_to_str(c_comment)
    a = none_to_str(a)
    b = none_to_str(b)
    c = none_to_str(c)
    discriminant = none_to_str(discriminant)
    return render(request, 'quadratic/result.html', {
            'a': a,'b': b,'c': c, 'discriminant':discriminant,
            'root_message':root_message, 'a_comment': a_comment,
            'b_comment': b_comment, 'c_comment': c_comment
        })

def check_in_reques(param, request):
    value = None
    if param not in request.GET:
        value = 'коэффициент не найден!'
    elif not request.GET[param]:
        value = 'коэффициент не определен!'
    return value
def check_is_digit(value, first_param=False):
    result = ''
    try:
        int(value)
    except ValueError:
        return 'коэффициент не целое число'
    if value.find('.') >= 0:
        return 'коэффициент не целое число'
    elif first_param and int(value) == 0:
        return 'коэффициент при первом слагаемом уравнения не может быть равен нулю'
    #else: value = int(value)
    return ''
"""
def none_to_str(var):
    print var
    if var is None:
        var = ''
    return var

