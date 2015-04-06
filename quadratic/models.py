#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models

def find_zero(a):
    try:
        if int(a) == 0:
            return "Коэффициент при первом слагаемом не может быть равен нулю"
    except: pass

def find_exception(p):
    if p == '':
        return "Коэффициент не определен"
    elif not p.replace('.', '').replace('-', '').isdigit():
        return "Коэффициент не целое число"

def get_discr(a, b, c):
    try:
        if int(a) != 0:
            d = int(b)**2 - 4*int(a)*int(c)
            return d
    except: pass

def get_eq_root(a, b, d):
    try:
        if int(d) < 0:
            return "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений"
        elif int(d) == 0:
            x = -int(b) / 2*int(a)
            return "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: %.1f" %x
        else:
            x1 = (-int(b) + d ** 0.5) / 2 * int(a)
            x2 = (-int(b) - int(d) ** 0.5) / 2 * int(a)
            return "Квадратное уравнение имеет два действительных корня: x1=%.1f, x2=%.1f" %(x1, x2)
    except: pass





