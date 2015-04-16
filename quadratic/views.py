#!/usr/bin/python		
# -*- coding: UTF-8 -*-

from django.shortcuts import render

def quadratic(request):
    return render(request, 'quadratic/quadratic.html')

def results(request):
#http://stackoverflow.com/questions/150505/capturing-url-parameters-in-request-get
    a=request.GET.get('a', '')
    b=request.GET.get('b', '')
    c=request.GET.get('c', '')

    def a_exists(number):
        try:
            return int(number.replace('-',''))==0#no float parameters possible! only negative and positive integers.
        except Exception:
            return False  

    def coeff_correct(number):
        msg=''
        if number=='':
            msg='коэффициент не определен'
        elif not number.replace('-','').isdigit(): #no float parameters possible! only negative and positive integers.
        #elif not coeff.isdigit():
            msg='коеффициент не целое число'
        return msg
         

    #if int(a)==0: #a-parameter should necessarily exist
    if a_exists(a): #It WORKS if no a-paramater defined
    #if coefficient(a.replace('-','')) != "": #a_exists() function defined instead, no need to develop business-logics at this direction
        a_msg='коеффициент при первом слагаемом уравнения не может быть равен нулю'
    else:
        a_msg=coeff_correct(a)
    b_msg=coeff_correct(b)
    c_msg=coeff_correct(c)
    message=""
    discriminant=0 #to render the discriminant variable in case of the empty message variable
    if a_msg==b_msg==c_msg=="":
        a = int(a)
        b = int(b)
        c = int(c)
        discriminant=b**2-4*a*c
        if discriminant<0:
            message='Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
        elif discriminant==0:
            x=round(float(-b/(2.0*a)), 2)
            message='Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s' % x
        else:
            x1=round(float((-b+(b**2-4*a*c)**0.5)/2.0*a), 2)
            x2=round(float((-b-(b**2-4*a*c)**0.5)/2.0*a), 2)
            message='Квадратное уравнение имеет два действительных корня: х1 = %s , x2 = %s' % (x1, x2)
    return render(request, 'quadratic/results.html', { 'list':(('a',a,a_msg),('b',b,b_msg),('c',c,c_msg)), 'message':message, 'discriminant':discriminant}) #discriminant = 0 in case of empty message-variable: improve your code! (need to avoid zero-equal D if any parameter defined incorrectly)
