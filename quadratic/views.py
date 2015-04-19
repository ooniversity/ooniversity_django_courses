# -*- coding: utf-8 -*-

from django.shortcuts import render
from forms import QuadraticForm

def quadratic_result(request):
     
    d = {}
    
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            discriminant = count_discriminant(**data)
            if discriminant < 0:
                result_message = "Дискриминант меньше нуля, квадратное уравнение не имеет действительный решений."
            elif discriminant == 0:
                x = (- data['b']) / (2.0 * data['a'])
                result_message = "Дискриминант равен нулю, квадратное уравнение имеет один корень: x1 = x2 = %d" % x
            else:
                x1 = (- data['b'] + discriminant**0.5) / (2.0 * data['a'])
                x2 = (- data['b'] - discriminant**0.5) / (2.0 * data['a'])
                result_message = "Квадратное уравнение имеет два действительный корня: x1 = " + str(x1) + ", x2 = " + str(x2)
            d.update({'discriminant': discriminant, 'message': result_message})
    else:
        form = QuadraticForm()
    d.update({'form':form})
 
    return render(request, 'quadratic/results.html', d)


def count_discriminant(a, b, c):
    d = b**2.0 - 4.0 * a * c
    return d
