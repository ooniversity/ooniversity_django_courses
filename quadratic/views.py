# -*- coding: utf-8 -*-

from django.shortcuts import render
from quadratic import check_coef, solve_quadratic_equation, get_discr
from django import forms
from django.shortcuts import render, redirect


class QuadraticForm(forms.Form):
    a = forms.FloatField(label="Коэффициент a:")
    b = forms.FloatField(label="Коэффициент b:")
    c = forms.FloatField(label="Коэффициент c:")

    def clean_a(self):
        a = self.cleaned_data.get('a')
        if a == 0:
            raise forms.ValidationError("Коэффициент при первом слагаемом не может быть равным нулю.")
        return a


def results(request):
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data.get('a')
            b = form.cleaned_data.get('b')
            c = form.cleaned_data.get('c')
            text = '\n\nДискриминант: {0}\n\n'.format(get_discr(a, b, c))
            text += solve_quadratic_equation(a, b, c)
            return render(request, "quadratic/quadratic.html", {'form': form, 'text': text})
        else:
            return render(request, "quadratic/quadratic.html", {'form': form})            
    else:
        form = QuadraticForm()
        return render(request, "quadratic/quadratic.html", {'form': form})



"""
def results(request):
    a = request.GET.get('a', '')
    b = request.GET.get('b', '')
    c = request.GET.get('c', '')
    text = 'Квадратное уравнение a*x*x + b*x + c = 0\n'
    text += '\n• a = {0}'.format(a)
    text += check_coef(a, isA = True)
    text += '\n• b = {0}'.format(b)
    text += check_coef(b)
    text += '\n• c = {0}'.format(c)
    text += check_coef(c)
    if check_coef(a, isA = True) == '' and check_coef(b) == '' and check_coef(c) == '':
        text += '\n\nДискриминант: {0}\n\n'.format(get_discr(a, b, c))
        text += solve_quadratic_equation(a, b, c)
    return HttpResponse (text, content_type="text/plain; charset=utf-8")
"""


