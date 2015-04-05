# -*- coding: utf-8 -*-

from django.shortcuts import render

def quadratic_results(request):
    list_variable = [
    {'name_get':'a', 'name_var':None, 'comment':'', 'first_param':True},
    {'name_get':'b', 'name_var':None, 'comment':'', 'first_param':False},
    {'name_get':'c', 'name_var':None, 'comment':'', 'first_param':False}
    ]
    for s in list_variable:
        check_all(request, s)

    a = list_variable[0]['name_var']
    b = list_variable[1]['name_var']
    c = list_variable[2]['name_var']

    a_comment = list_variable[0]['comment']
    b_comment = list_variable[1]['comment']
    c_comment = list_variable[2]['comment']

    #print a,b,c
    #print a_comment, b_comment,c_comment

    discriminant = None
    root_message = ''
    need_show_discriminant = False

    if not a_comment and not b_comment and not c_comment:
        need_show_discriminant = True
        discriminant = b*b - 4 * a * c
        if discriminant < 0:
            root_message = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
        elif int(discriminant) == 0:
            x = -b / 2 * a
            root_message = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {0:.1f}'.format(x)
        else:
            x1 = (-b + discriminant ** (1.0/2))/ 2 * a
            x2 = (-b - discriminant ** (1.0/2))/ 2 * a
            root_message = 'Квадратное уравнение имеет два действительных корня: x1 = {0:.1f}, x2 = {1:.1f}'.format(x1,x2)

    a = none_to_str(a)
    b = none_to_str(b)
    c = none_to_str(c)
    discriminant = none_to_str(discriminant)
    return render(request, 'quadratic/result.html', {
            'a': a,'b': b,'c': c, 'discriminant':discriminant,
            'root_message':root_message, 'a_comment': a_comment,
            'b_comment': b_comment, 'c_comment': c_comment,
            'need_show_discriminant':need_show_discriminant
        })

def check_all(request, list_var):
    list_var['comment'] = check_request_get(request, list_var['name_get'])
    if not list_var['comment']:
        list_var['name_var'] = request.GET[list_var['name_get']]
        list_var['comment'] = check_int(list_var['name_var'], list_var['comment'], list_var['first_param'])
        if not list_var['comment']:
            list_var['name_var'] = int(list_var['name_var'])


def check_request_get(request, param):
    comment = ''
    if param not in request.GET:
        comment = 'коэффициент не найден!'
    elif not request.GET[param]:
        comment = 'коэффициент не определен!'
    return comment

def check_int(variable, comment, first_param=False):
    new_comment = ''
    try:
        int(variable)
    except ValueError:
        new_comment = 'коэффициент не целое число'
    except TypeError:
        print 'variable is None'
    if variable and not new_comment:
        if variable.find('.') >= 0:
            new_comment = 'коэффициент не целое число'
        elif int(variable) == 0 and first_param:
            new_comment = 'коэффициент при первом слагаемом уравнения не может быть равен нулю'
    return new_comment

def none_to_str(var):
    if var is None:
        var = ''
    return var
