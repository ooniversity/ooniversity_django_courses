# -*- coding: utf-8 -*-

from django.shortcuts import render

def quadratic_result(request):
    a = str(request.GET['a'])
    b = str(request.GET['b'])
    c = str(request.GET['c'])
    
       
    a_checked, l1 = check_a(a)
    b_checked, l2 = check_bc(b)
    c_checked, l3 = check_bc(c)
    print a_checked, b_checked, c_checked,
    print l1, l2, l3
    
    d = {}
    
    if a_checked and b_checked and c_checked and a_checked != 0 and str(a_checked).replace('-','').isdigit() and str(b_checked).replace('-','').isdigit() and str(c_checked).replace('-','').isdigit():
        disc = count_disc(a_checked, b_checked, c_checked)
        if disc == 0:
            str_disc = "Дискриминант: 0"
            x1 = (- b_checked) / (2.0 * a_checked)
            str_root = "Дискриминант равен нулю, квадратное уравнение имеет один корень: x1 = x2 = " + str(x1)
            d = {'var': [a_checked, b_checked, c_checked], 'strings': [l1, l2, l3], 'discs': [str_disc, str_root]}
        elif disc < 0:
            str_disc = "Дискриминант: " + str(disc)
            str_root = "Дискриминант меньше нулю, квадратное уравнение не имеет действительный решений."
            d = {'var': [a_checked, b_checked, c_checked], 'strings': [l1, l2, l3], 'discs': [str_disc, str_root]}
        else:
            str_disc = "Дискриминант: " + str(disc)
            x1 = (- b_checked + disc**0.5) / (2.0 * a_checked)
            x2 = (- b_checked - disc**0.5) / (2.0 * a_checked)
            str_root = "Квадратное уравнение имеет два действительный корня: x1 = " + str(x1) + ", x2 = " + str(x2)
            d = {'var': [a_checked, b_checked, c_checked], 'strings': [l1, l2, l3], 'discs': [str_disc, str_root]}
    else:
        d = {'var': [a_checked, b_checked, c_checked], 'strings': [l1, l2, l3], 'discs': ['', '']}
            
    return render(request, 'quadratic/results.html', {'disc': d}  )



def count_disc(a, b, c):
    d = b**2.0 - 4.0 * a * c
    return d


def check_a(a):
    if a:
        if a.replace('-','').isdigit():
            a = int(a)
            if a != 0:
                return a, ''
            else:
                return 0, 'коэффициент при первом слогаемом уравнения не может быть равным нулю'
        else:
            return a, 'коэффициент  не целое число'
    else:
        return '', 'коэффициент не определен'



def check_bc(bc):
    if bc:
        if bc.replace('-','').isdigit():
            bc = int(bc)
            return bc, ''
        else:
            return bc, 'коэффициент  не целое число'
    else:
        return '', 'коэффициент не определен'


