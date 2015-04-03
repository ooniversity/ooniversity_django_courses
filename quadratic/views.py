#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.shortcuts import render

def quadratic(request):
    return render(request, 'quadratic.html')

def results(request):
    try:
        a=request.GET['a']
    except KeyError:
        a=''
    try:
        b=request.GET['b']
    except KeyError:
        b=''
    try:
        c=request.GET['c']
    except KeyError:
        c=''
    def check(cof):
        com=''
        if cof=='':
            com='коэффициент не определен'
        elif not cof.replace('-','').replace('.','').isdigit():
            com='коеффициент не целое число'
        return com
    if a=='0':
        a_com='коеффициент при первом слогаемом уравнения не может быть равным нулю'
    else:
        a_com=check(a)
    b_com=check(b)
    c_com=check(c)
    answer=''
    if a_com==b_com==c_com==answer:
        a,b,c=float(a),float(b),float(c)
        dis=b**2-4*a*c
        if dis<0:
            answer='Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
        elif dis==0:
            x=-b/(2.0*a)
            answer='Дискриминант равен нулю квадратное уравнение имеет один действительный корень: x1 = x2 %d' % x
        else:
            x1=(-b+(b**2-4*a*c)**0.5)/2.0*a
            x2=(-b-(b**2-4*a*c)**0.5)/2.0*a
            answer='Квадратное уравнение имеет два действительных корня: х1 = %d , x2 = %d' % (x1, x2)
    return render(request, 'results.html', { 'list':(('a',a,a_com),('b',b,b_com),('c',c,c_com)), 'answer':answer})
