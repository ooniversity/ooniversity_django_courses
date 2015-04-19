# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django import forms

class QuadraticForm(forms.Form):
    a = forms.FloatField(label="Коэффициент a")
    b = forms.FloatField(label="Коэффициент b")
    c = forms.FloatField(label="Коэффициент c")

    def clean_a(self):
                data = self.cleaned_data['a']
                if data == 0.0:
                    raise forms.ValidationError("коэффициент при первом слагаемом не может быть равным 0")
                return data

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
    context = {}
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data.get('a')
            b = form.cleaned_data.get('b')
            c = form.cleaned_data.get('c')
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
            context.update({'form':form})
            return render(request, 'quadratic/results.html', context)

    else:
        form = QuadraticForm()
    return render(request, 'quadratic/results.html', {'form':form})





