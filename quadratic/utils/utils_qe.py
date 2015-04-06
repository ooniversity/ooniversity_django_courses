# -*- coding: utf-8 -*-

"""
В данном модуле находятся все необходимые инструменты для решения квадратного уравнения.

Квадратное уравнение - алгебраическое уравнение общего вида:

    ax^2 + bx + c = 0,

где x — свободная переменная, a, b, c — коэффициенты уравнения.

Выражение ax^2 + bx + c называется квадратным трёхчленом.

Корень - это значение переменной x, обращающее квадратный трёхчлен в ноль, а квадратное уравнение в верное равенство.

Элементы квадратного уравнения имеют собственные названия:
    a - первый или старший коэффициент,
    b - второй или коэффициент при x,
    c - свободный член.
"""


# Проверка валидности параметров квадратного уравнения

def check_param(parametr):
    sign = 1
    if parametr.startswith('-'):
        parametr = parametr[1:]
        sign = -1
    if not parametr.isdigit():
        if parametr == '':
            return 'not defined'
        return 'not digit'
    else:
        return int(parametr) * sign


# Функция нахождения дискрименанта

def get_discr(a, b, c):
    d = b**2 - 4 * a * c
    return d


# Получение корней квадратного уравнения

def get_eq_root(a, b, d, order = 1):
    if order == 1:
        x = (-b + d ** (1/2.0)) / 2 * a
    else:
        x = (-b - d ** (1/2.0)) / 2 * a
    return x


# Функция решения квадратного уравнения

def quadratic_equ(p1, p2, p3):
    dict_result = {'a': 'none', 'b': 'none', 'c': 'none', 'd': '', 'x_1': 'none', 'x_2': 'none', 'result': 'none'}

    # Определение коефициентов
    dict_result['a'] = check_param(p1)
    dict_result['b'] = check_param(p2)
    dict_result['c'] = check_param(p3)
    if dict_result['a'] == 0:
        dict_result['a'] = 'first parametr is zero'

    # Решение квадратного уравнения
    if type(dict_result['a']) is int and type(dict_result['b']) is int and type(dict_result['c']) is int:
        dict_result['d'] = get_discr(dict_result['a'], dict_result['b'], dict_result['c'])
        if dict_result['d'] < 0:
            dict_result['result'] = 'discrim less zero'
        elif dict_result['d'] == 0:
            dict_result['x_1'] = get_eq_root(dict_result['a'], dict_result['b'], dict_result['d'])
            dict_result['x_2'] = dict_result['x_1']
            dict_result['result'] = 'One root'
        else:
            dict_result['x_1'] = get_eq_root(dict_result['a'], dict_result['b'], dict_result['d'])
            dict_result['x_2'] = get_eq_root(dict_result['a'], dict_result['b'], dict_result['d'], 2)
            dict_result['result'] = 'Two roots'
    return dict_result
