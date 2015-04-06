#coding: utf-8
class QuadraticEquation(object):
    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)

    def calc_discr(self):
        self.d = self.b ** 2 - 4 * self.a * self.c

    def get_discr(self):
        return self.d

    def get_eq_root(self, order = 1):
        if order == 1:
            return (-self.b + self.d ** (1/2.0)) / 2 * self.a
        else:
            return (-self.b - self.d ** (1/2.0)) / 2 * self.a

def check_coef(coef, isA = False):
    if coef == '':
        return '\nкоэффициент не определён'
    try:
        coef = int(coef)
    except ValueError:
        return '\nкоэффициент не целое число'
    if isA == True:
        if coef == 0:
            return '\nкоэффициент при первом слагаемом не может быть равным нулю'
    return ''

def solve_quadratic_equation(a, b, c):
    eq = QuadraticEquation(a, b, c)
    eq.calc_discr()
    if eq.get_discr() < 0:
        return 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    elif eq.get_discr() == 0:
        return 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: х1 = х2 = {0}'.format(eq.get_eq_root())
    else:
        return 'Квадратное уравнение имеет два действительных корня: х1 = {0}, х2 = {1}'.format(eq.get_eq_root(), eq.get_eq_root(order = 2))

def get_discr(a, b, c):
    eq = QuadraticEquation(a, b, c)
    eq.calc_discr()
    return eq.get_discr()
