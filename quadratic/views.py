# coding: utf8

from django.shortcuts import render
from django import forms


class QuadraticForm(forms.Form):
    a = forms.FloatField(
        label='Коэффициент a:', error_messages={'required': 'Введите коэффициент!'})
    b = forms.FloatField(
        label='Коэффициент b:', error_messages={'required': 'Введите коэффициент!'})
    c = forms.FloatField(
        label='Коэффициент c:', error_messages={'required': 'Введите коэффициент!'})

    def clean_a(self):
        value = self.cleaned_data['a']
        if value == 0:
            raise forms.ValidationError(
                "Коэффициент при первом слогаемом в уравнении не может быть равен нулю")
        return value


def discr(a, b, c):
    pretenz_discr = b ** 2 - 4 * a * c
    result = round(pretenz_discr, 3)
    return result


def get_roots(a, b, c):
    if discr(a, b, c) >= 0:
        pretenz_x1 = (-b - discr(a, b, c) ** 0.5) / 2 * a
        pretenz_x2 = (-b + discr(a, b, c) ** 0.5) / 2 * a

        x1 = round(pretenz_x1, 3)
        x2 = round(pretenz_x2, 3)
        return (x1, x2)


def quadratic_results(request):
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data.get('a')
            b = form.cleaned_data.get('b')
            c = form.cleaned_data.get('c')

            return render(request, "quadratic_results.html", {'form': form, 'discr': discr(a, b, c), 'roots': get_roots(a, b, c)})
    else:
        form = QuadraticForm()
    return render(request, "quadratic_results.html", {'form': form})
