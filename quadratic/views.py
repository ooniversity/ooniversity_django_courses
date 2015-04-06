# -*- coding: UTF8 -*-

from django.shortcuts import render
import math


def quadratic_results(request):

    #a,b,c = input("Enter the coefficients of a, b and c separated by commas: ")

    amsg=""
    bmsg=""
    cmsg=""
    dmsg=""
    text=""
    b=""
    c=""
    d=""
    mya=0
    myb=0
    myc=0
    err=0

    a = request.GET['a']
    if a=="":
       amsg='коэффициент не определен'
       err=1
    else:
        if a=="0":
            amsg='коэффициент при первом слагаемом уравнения не может быть равным нулю'
            err=1
        else:
            if a[0]=='-':
                aa=a[1:]
            else:
                aa=a
            if aa.isdigit()==False:
                amsg='коэффициент не целое число'
                err=1
            else:
                mya=int(a)

    b = request.GET['b']
    if b=="":
       bmsg='коэффициент не определен'
       err=1
    else:
        if b[0]=='-':
            bb=b[1:]
        else:
            bb=b
        if bb.isdigit()==False:
            bmsg='коэффициент не целое число'
            err=1
        else:
            myb=int(b)

    c = request.GET['c']
    if c=="":
       cmsg='коэффициент не определен'
       err=1
    else:
        if c[0]=='-':
            cc=c[1:]
        else:
            cc=c
        if cc.isdigit()==False:
            cmsg='коэффициент не целое число'
            err=1
        else:
            myc=int(c)

    if err==0:
        d = myb**2-4*mya*myc # discriminant

        if d < 0:
            dmsg=str(d)
            text="Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений"
        elif d == 0:
            x = (-myb+math.sqrt(myb**2-4*mya*myc))/2*mya
            text = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень x1 = x2 = " + str(x)
        else:
            x1 = (-myb+math.sqrt(myb**2-4*mya*myc))/2*mya
            x2 = (-myb-math.sqrt(myb**2-4*mya*myc))/2*mya
            text = "Квадратное уравнение имеет два действительных корня : x1 = " + str(x1) + ", x2 = " + str(x2)


    return render(request, 'results.html', {'a' : a, 'amsg' : amsg, 'b' : b, 'bmsg' : bmsg, 'c' : c, 'cmsg' : cmsg, 'dsmg' : dmsg, 'text' : text })


