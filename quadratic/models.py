#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models


def find_exception(coefficient, value):
    if not value:
        return "Коэффициент не определен"

    try:
        value = int(value)
    except ValueError:
        return "Коэффициент не целое число"
        
    if coefficient == 'a' and value == 0:
        return "Коэффициент при первом слагаемом уравнения не может быть равным нулю"


def get_discr(a, b, c):
    d = int(b)**2 - 4*int(a)*int(c)
    return d 


def get_eq_root(a, b, d):
    if int(d) < 0:
        return "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений"
    elif int(d) == 0:
        x = -int(b) / 2*int(a)
        return "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1=x2=%.1f" %x
    else:
        x1 = (-int(b) + d ** 0.5) / 2 * int(a)
        x2 = (-int(b) - int(d) ** 0.5) / 2 * int(a)
        return "Квадратное уравнение имеет два действительных корня: x1=%.1f, x2=%.1f" %(x1, x2)
