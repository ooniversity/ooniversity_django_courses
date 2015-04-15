# -*- coding: utf-8 -*-
from django.shortcuts import render
from utils import utils
from django import forms
from django.core import validators

# Create your views here.

#Создаем класс, который будет формой для задания коефициентов квадратного уравнения
class QuadraticForm(forms.Form):
    a = forms.FloatField(required=True, label='коеффициент а')
    b = forms.FloatField(required=True, label='коеффициент b')
    c = forms.FloatField(required=True, label='коеффициент c')

    def valid_a(self, var):
        data = var
        if data == 0:
            raise forms.ValidationError("You have forgotten about Fred!")
        # Always return the cleaned data, whether you have changed it or
        # not.
        return data


def quadratic_results (request):
    #Инстанцируем форму
    form = QuadraticForm()
    #Делаем так, чтобы значение после GET-запроса(нажали на Решить)
    #не исчезали, а оставались в полях. Чтобы пользователь не вводил данные много раз
    #есть данные были не корректные
    if request.method == "GET":
        form = QuadraticForm(request.GET)
        #Проверка данных на правильность (валидность)
        if form.is_valid():
            form.valid_a(form.cleaned_data['a'])
            #print form.cleaned_data Джанго сохраняет очищенные данные в переменной cleaned_data
            #Вызываем функция quadratic_equel, которая посчитает квадратное уравнение
            #Функция возвращаем словать со всеми значениями, которые нужно будет передать на WEB
            #Мне показалось, что так удобне
            dict_quadr = utils.quadratic_equel(form.cleaned_data['a'], form.cleaned_data['b'], form.cleaned_data['c'])
        else:
            dict_quadr = {}
    else:
        form = QuadraticForm(request.POST)

    #context = {'a_native':request.GET.get('a'), 'b_native':request.GET.get('b'), 'c_native':request.GET.get('c'), }
    context = {'diction':dict_quadr, 'form':form, }
    #Отображаем HTML страничку и передаем ей все необходимие переменные
    return render (request, 'quadratic/index_quadratic.html', context)
