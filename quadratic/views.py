# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from utils import utils


def quadratic_results (request):
    #Вызываем функция quadratic_equel, которая посчитает квадратное уравнение
    #Функция возвращаем словать со всеми значениями, которые нужно будет передать на WEB
    #Мне показалось, что так удобней
    dict_quadr = utils.quadratic_equel(request.GET['a'], request.GET['b'], request.GET['c'])

    #Парсим HTML страничку и передаем ей все необходимие переменные
    return render (request, 'quadratic/index_quadratic.html',
        {'a_native':request.GET['a'], 'b_native':request.GET['b'], 'c_native':request.GET['c'],  'diction':dict_quadr},)
