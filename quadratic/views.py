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

    def clean_a(self):
        data = self.cleaned_data['a']
        #Кастомизированная валидация параметров
        if data == 0:
            raise forms.ValidationError("Коеффициент при первом слагаемом \
                                        уравнения не может быть равным 0")
        return data


def quadratic_results (request):
    #Инстанцируем форму
    form = QuadraticForm()
    diction = {}
    #Делаем так, чтобы значение после GET-запроса(нажали на Решить)
    #не исчезали, а оставались в полях. Чтобы пользователь не вводил
    #данные много раз есть данные были не корректные
    if request.GET.get('a') != None and request.GET.get('b') != None \
       and request.GET.get('c') != None:
        if request.method == "GET":
            form = QuadraticForm(request.GET)
            #Проверка данных на правильность (валидность)
            if form.is_valid():
                #print form.cleaned_data Джанго сохраняет очищенные данные в
                #переменной cleaned_data
                #Вызываем функция quadratic_equel, которая посчитает квадратное
                #уравнение
                #Функция возвращаем словать со всеми значениями, которые нужно
                #будет передать на WEB
                #Мне показалось, что так удобне
                diction = utils.quadratic_equel(form.cleaned_data['a'],
                                                form.cleaned_data['b'],
                                                form.cleaned_data['c'])
        else:
            form = QuadraticForm()
    context = {'diction':diction, 'form':form,}
    return render (request, 'quadratic/index_quadratic.html', context) #Отображаем HTML страничку и передаем ей все необходимие переменные


