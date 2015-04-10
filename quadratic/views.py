#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.shortcuts import render


def quadratic(request):
    return render(request, 'quadratic/quadratic.html')


def results(request):
    a = request.GET.get('a', '').replace(',', '.')
    b = request.GET.get('b', '').replace(',', '.')
    c = request.GET.get('c', '').replace(',', '.')

    def check(cof):
        com = ''
        if cof == '':
            com = u'коэффициент не определен'
        elif not cof.strip().lstrip('-').replace('.', '', 1).isdigit() and not cof.strip().lstrip('+').replace('.', '', 1).isdigit():
            com = u'коеффициент не целое число'
        return com

    def iszero(i):
        try:
            return int(a.lstrip('-').replace('.', '', 1)) == 0
        except ValueError:
            return False

    def int_or_float(num):
        return int(float(num)) if int(float(num)) == float(num) else float(num)

    if iszero(a):
        a_com = u'коеффициент при первом слогаемом уравнения не может быть равным нулю'
    else:
        a_com = check(a)
    b_com = check(b)
    c_com = check(c)
    answer = ''
    if a_com == b_com == c_com == answer:
        a = int_or_float(a)
        b = int_or_float(b)
        c = int_or_float(c)
        dis = b ** 2 - 4 * a * c
        if dis < 0:
            answer = u'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
        elif dis == 0:
            x = int_or_float(round(-b / (2.0 * a), 3))
            answer = u'Дискриминант равен нулю квадратное уравнение имеет один действительный корень: x1 = x2 = %s' % x
        else:
            x1 = int_or_float(round((-b + (b ** 2 - 4 * a * c) ** 0.5) / 2.0 * a, 3))
            x2 = int_or_float(round((-b - (b ** 2 - 4 * a * c) ** 0.5) / 2.0 * a, 3))
            answer = u'Квадратное уравнение имеет два действительных корня: х1 = %s , x2 = %s' % (x1, x2)
    return render(request, 'quadratic/results.html', {'list': (('a', a, a_com), ('b', b, b_com), ('c', c, c_com)), 'answer': answer})
