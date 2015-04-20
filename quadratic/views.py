# ~*~ coding: utf-8 ~*~

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from django import forms

class QuadraticForm(forms.Form):

    a = forms.IntegerField(label='коээфициент a:')
    b = forms.IntegerField(label='коээфициент b:')
    c = forms.IntegerField(label='коээфициент c:')
    def clean_a(self):
        data = self.cleaned_data['a']
        if  data == 0:
            raise forms.ValidationError("Коэффициент ''а'' не может быть равен нулю.")

        # Always return the cleaned data, whether you have changed it or
        # not.
        return data


def resolve(request):
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
    if request.method == 'POST':
        form = QuadraticForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            dic = form.cleaned_data



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
                str_a = 'a = ' + a
                ia = dic[u'a']


            if dic.has_key(u'b'):
                b= str(dic[u'b'])
                str_b = 'b = ' + b
                ib = dic[u'b']


            if dic.has_key(u'c'):
                c= str(dic[u'c'])
                str_c = 'c = ' + c
                ic = dic[u'c']


            if ierr == 0:
                s0 = a + 'x**2 '
                if ia == 1: s0 = 'x**2 '
                if ia == -1: s0 = '-x**2 '
                s1 = b + 'x '
                if ib > 0: s1 = '+'+ b + 'x '
                if ib == 0: s1 = ''
                s2 = c
                if ic > 0: s2 = '+ '+c
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

    else:
        form = QuadraticForm()
    context = RequestContext(request, {
    'form': form,
    'titl': titl,
    'str_a': str_a,
    'str_b': str_b,
    'str_c': str_c,
    'str_D': str_D,
    'str_x': str_x
     })


    return HttpResponse(template.render(context))

