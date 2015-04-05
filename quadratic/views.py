# ~*~ coding: utf-8 ~*~

from django.http import HttpResponse
from django.template import RequestContext, loader

from django.shortcuts import render_to_response
#from pybursa_app.models import Student




def resolve(request):

    dic = request.GET

    template = loader.get_template('quadratic.html')



    err = '  - ошибка:'
    err2 = ' коэффициент "а" не может быть равен 0.'
    err3 = ' не введен коэффициент '
    err4 = ' коэффициент "а" не число'
    err5 = ' коэффициент "b" не число'
    err6 = ' коэффициент "c" не число'
    titl = ''
    str_x= ''
    str_D= ''
    ierr = 0
    ier2 = 0
    str_a = ''
    str_b = ''
    str_c = ''
    if dic.has_key(u'a'):
        a= str(dic[u'a'])
        aa = a.rstrip('/')
        str_a = 'a = ' + aa
        try:
            ia = int(aa)
        except ValueError:
            str_a += err + err4
            ierr = 1
        if ierr == 0 and ia == 0:
            ierr = 4
            str_a += err + err2
    else:
        str_a = err + err3 + 'a'
        ierr =1

    if dic.has_key(u'b'):
        b= str(dic[u'b'])
        bb = b.rstrip('/')
        str_b = 'b = ' + bb
        try:
            ib = int(bb)
        except ValueError:
            str_b += err + err5
            ierr = 2
    else:
        str_b = err + err3 + 'b'
        ierr =2

    if dic.has_key(u'c'):
        c= str(dic[u'c'])
        cc = c.rstrip('/')
        str_c = 'c = ' + cc
        try:
            ic = int(cc)
        except ValueError:
            str_c += err + err6
            ierr = 3
    else:
        str_c = err + err3 + 'c'
        ierr = 3




    if ierr == 0:
        s0 = aa + 'x**2 '
        if ia == 1: s0 = 'x**2 '
        if ia == -1: s0 = '-x**2 '
        s1 = bb + 'x '
        if ib > 0: s1 = '+'+ bb + 'x '
        if ib == 0: s1 = ''
        s2 = cc
        if ic > 0: s2 = '+ '+cc
        if ic == 0: s2 = ''
        titl = 'уравнение: '+ s0 + s1 + s2 + ' = 0'

        D = float(ib*ib-4*ia*ic)
        str_D = 'Дискриминант равен '+str(D)
        str_x = ''
        if D >= 0:
            x1 = (-ib + D**0.5)/(2*ia)
            x2 = (-ib - D**0.5)/(2*ia)
        if D > 0: str_x = 'Уравнение имеет два действительных корня Х1='+ str(x1)+' и Х2='+str(x2)
        if D == 0: str_x = 'Уравнение имеет один действительный корень Х1=Х2='+str(x1)
        if D < 0: str_x = 'Уравнение не имеет действительных корней'


    context = RequestContext(request, {
        'titl': titl,
        'str_a': str_a,
        'str_b': str_b,
        'str_c': str_c,
        'str_D': str_D,
        'str_x': str_x
    })

    return HttpResponse(template.render(context))
