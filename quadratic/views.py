# -*- coding: utf-8 -*-
from django.shortcuts import render


class Coefficient(object):

    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.value_int = None
        self.error_message = None

    def is_valid(self):
        if not self.value:
            self.error_message = "коэффициент не определен"
            return False

        try:
            self.value_int = int(self.value)
        except ValueError:
            self.error_message = "коэффициент не целое число"
            return False

        if self.name == 'a' and self.value_int == 0:
            self.error_message = "коэффициент при первом слагаемом уравнения не может быть равным нулю"
            return False
        return True


def get_discr(a, b, c):
    d = b**2 - 4*a*c
    return d


def get_eq_root(a, b, d, order=1):
    if order == 1:
        x = (-b + d**(1/2.0)) / 2*a
    else:
        x = (-b - d**(1/2.0)) / 2*a
    return x


def quadratic_results(request):
    context = {'error': False}
    for name_value in ['a', 'b', 'c']:
        coefficient = Coefficient(name_value, request.GET.get(name_value, ''))
        if coefficient.is_valid():
            context[name_value] = coefficient.value_int
        else:
            context['error'] = True
            context[name_value + '_error'] = coefficient.error_message
            context[name_value] = coefficient.value
    if not context['error']:
        a = context['a']
        b = context['b']
        c = context['c']
        d = get_discr(a, b, c)
        if d < 0:
            result_message = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
        elif d == 0:
            x = get_eq_root(a, b, d)
            result_message = "Дискриминант равен нулю, квадратное уравнение имеет один действительных корень: x1 = x2 = {}".format(x)
        else:
            x1 = get_eq_root(a, b, d)
            x2 = get_eq_root(a, b, d, order=2)
            result_message = "Квадратное уравнение имеет два действительных корня: x1 = {}, x2 = {}".format(x1, x2)

        context.update({'d': d, 'result_message': result_message})
    return render(request, 'quadratic/results.html', context)
