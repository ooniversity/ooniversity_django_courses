# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect

from forms import QuadraticForm


def quadratic_results(request):
    discriminant = None
    root_message = ''

    form = QuadraticForm()
    if request.method == "GET" and request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            a = data['a']
            b = data['b']
            c = data['c']
            discriminant = b*b - 4 * a * c
            if discriminant < 0:
                root_message = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
            elif int(discriminant) == 0:
                x = -b / 2 * a
                root_message = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: \
                x1 = x2 = {0:.1f}'.format(x)
            else:
                x1 = (-b + discriminant ** (1.0/2))/ 2 * a
                x2 = (-b - discriminant ** (1.0/2))/ 2 * a
                root_message = 'Квадратное уравнение имеет два действительных корня: x1 = {0:.1f}, \
                x2 = {1:.1f}'.format(x1, x2)

    return render(request, 'quadratic/result.html',
                  {'discriminant': discriminant,
                   'root_message': root_message,
                   'form': form
                   })
