#coding: utf-8
class QuadraticEquation(object):

    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)

    def calc_discr(self):
        self.d = self.b ** 2 - 4 * self.a * self.c
        #return self.d

    def get_discr(self):
        return self.d

    def get_eq_root(self, order=1):
        if order == 1:
            return (-self.b + self.d ** (1/2.0)) / 2 * self.a
        else:
            return (-self.b - self.d ** (1/2.0)) / 2 * self.a

    def solve(self):

        if self.get_discr() < 0:
            return 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'

        elif self.get_discr() == 0:
            return 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: х1 = х2 = %3.1f'\
                   % (self.get_eq_root())

        else:
            return 'Квадратное уравнение имеет два действительных корня:х1 = %3.1f, х2 = %3.1f'\
                   % (self.get_eq_root(), self.get_eq_root(order=2))