#coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
from quadratic import *


def check_a(a):
    if not a:
        return '\n коэффициент не определён'

    if not a[-1].isdigit():
        return '\n коэффициент не целое число'
    elif int(a) == 0:
        return '\n коэффициент при первом слагаемом не может быть равным нулю'


def check_other(a):
    if not a:
        return '\n коэффициент не определён'

    if not a[-1].isdigit():
        return '\n коэффициент не целое число'


def results(request):
    # checking variables
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']

    output = 'Квадратное уравнение a*x*x + b*x + c = 0\n\n'

    output += 'a = %s' % str(a)
    try:
        output += check_a(a)
    except TypeError:
        pass

    output += '\nb = %s' % str(b)
    try:
        output += check_other(b)
    except TypeError:
        pass

    output += '\nc = %s' % str(c)
    try:
        output += check_other(c)
    except TypeError:
        pass

    # solution to equation
    if check_a(a) is None and check_other(b) is None and check_other(c) is None:
        eq = QuadraticEquation(a, b, c)
        discr = eq.calc_discr()
        solve = eq.solve()

        output += '\n\nДискриминант: %d' % (eq.get_discr())
        output += '\n\n%s' % solve

    return HttpResponse(output, content_type="text/plain; charset=utf-8")