# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from quadratic import check_coef, solve_quadratic_equation, get_discr
"""
from django import forms
from django.shortcuts import redirect


class QuadraticForm(forms.Form):
    a = forms.FloatField(label="Coef A", help_text="Enter A")
    b = forms.FloatField()
    c = forms.FloatField()

Затем инстанс этого класса указать во вьюшке: form = QuadraticForm()
Включить form в состав переменных в render: 'form': form
В шаблоне страницы использовать {{ form }}, а лучше {{ form.as_p }} (чтобы не в одну строку)
В любом случае вставляем внутрь тега <form>, где есть <input type="submit">

Чтобы данные сохранялись в форме после отправки, надо во вьюшку добавить:

if request.method == 'POST':
    form = QuadraticForm(request.POST)
    if form.is_valid():
        print form.cleaned_data
        return redirect('/')   #или render формы с результатами
else:
    form = QuadraticForm(initial={'a': 1, 'b': 1, 'c': 1})

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
