# -*- coding: utf-8 -*-
from django.shortcuts import render
from django import forms

class QuadraticForm(forms.Form):
      a = forms.FloatField()
      b = forms.FloatField()
      c = forms.FloatField()


def quadratic(request):
      form = QuadraticForm()
      return render(request, 'quadratic.html', {'form':form})
def result(request):
      def get_parameter(parameter):
            try:
                 return request.GET[parameter]
            except:
                    return ''
      a = get_parameter('a')
      b = get_parameter('b')
      c = get_parameter('c')
      def check_parameter(parameter):
            status = ''
            if parameter == '':
               status = "Коэффициент не определен"
            elif not parameter.replace('-','',1).isdigit():
               status = "Коэффициент не целое число"
            print parameter, status
            return status
      a_status = check_parameter(a)
      if a_status == '':
           a = int(a)
      b_status = check_parameter(b)
      if b_status == '':
           b = int(b)
      c_status = check_parameter(c)
      if c_status == '':
           c = int(c)
      d_status = ''
      d = 0
      if a == 0:
           a_status = "Коэффициент первого члена не может быть равен нулю"
      elif a_status != 0 and b_status != "Коэффициент не целое число" and c_status != "Коэффициент  целое число":
          d = float(b*b - 4*a*c)
          if d > 0:
              x1 = float((-b + d**0.5) / 2*a)
              x2 = float((-b - d**0.5) / 2*a)
              d_status = "Уравнение имеет два действительных корня: x1 = %s, x2 = %s" % (x1,x2)
          elif d == 0:
              x1 = x2 = float(- b / 2*a)
              d_status = "Дискриминант равен нулю имеет один корень: x1 = x2 = %s" % x1
          else:
              d_status = "Дикриминант меньше нуля не имеет корней"
      return render(request, 'results.html', { 'a':[a,a_status], 'b':[b,b_status], 'c':[c,c_status], 'd':[d, d_status]} )