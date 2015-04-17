# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django import forms


class QuadraticForm(forms.Form):
    a = forms.FloatField(label="Коэффициент a", help_text='введите значение коэф. а')
    b = forms.FloatField(label="Коэффициент b", help_text='введите значение коэф. b')
    c = forms.FloatField(label="Коэффициент c", help_text='введите значение коэф. c')


    def clean_a(self):
        data = self.cleaned_data['a']
        if data == 0:
            raise forms.ValidationError("коэффициент при первом слагаемом не может быть равным 0")
        return data


def get_discr(a, b, c):
    return b**2 - 4 * a * c


def get_eq_root(a, b, c, order=1):
    d = get_discr(a, b, c)
    if order == 1:
        return (-b + d ** (1/2.0)) / 2 * a
    else:
        return (-b - d ** (1/2.0)) / 2 * a


def solve(a, b, c):
    if get_discr(a, b, c) < 0:
        return '\n \n Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    elif get_discr(a, b, c) == 0:
        return '\n \n Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: х1 = х2 = %3.1f'\
                   % (get_eq_root(a, b, c))
    else:
        return '\n \n Квадратное уравнение имеет два действительных корня:х1 = %3.1f, х2 = %3.1f'\
                   % (get_eq_root(a, b, c), get_eq_root(a, b, c, order=2))


def results_function(request):
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data.get('a')
            b = form.cleaned_data.get('b')
            c = form.cleaned_data.get('c')
            discr = '\n\nДискриминант: %3.1f' % get_discr(a, b, c)
            solv = solve(a, b, c)
            return render(request, "quadratic_results.html",
                          {'form': form, 'discr': discr, 'solv': solv})
        else:
            return render(request, "quadratic_results.html", {'form': form})
    else:
        form = QuadraticForm()
        return render(request, "quadratic_results.html", {'form': form})



'''
# old version

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
'''