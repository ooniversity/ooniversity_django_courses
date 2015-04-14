#!/usr/bin/env python
# coding: utf-8

from django.shortcuts import render


def validate(request, name):
    value = request.GET.get(name)
    if value == '' or value == None:
        return value, "Коэфициент не определен"

    try:
        return int(value), None
    except ValueError:
        return value, "Коэфициент не целое число"


def quadratic_results(request):
    a, a_error = validate(request, 'a')
    b, b_error = validate(request, 'b')
    c, c_error = validate(request, 'c')

    if a_error is None and a == 0:
            a_error = ("Коэфициент при первом слагаемом уравнении не может быть"
                " равен нулю")

    discr = None
    x1 = None
    x2 = None

    if not any([a_error, b_error, c_error]):
        discr = b ** 2 - 4 * a * c

        if discr == 0:
            x1 = x2 = float(-b) / 2 * a
        elif discr > 0:
            x1 = float(-b + discr ** 0.5) / (2 * a)
            x2 = float(-b - discr ** 0.5) / (2 * a)

    return render(request, 'quadratic_results.html', {
        'a': a,
        'b': b,
        'c': c,
        'discr': discr,
        'a_error': a_error,
        'b_error': b_error,
        'c_error': c_error,
        'x1': x1,
        'x2': x2,
    })
