# Quadratic

class Quadratic(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_discrim(self):
        self.d = self.b ** 2 - 4 * self.a * self.c

    def get_discrim(self):
        return self.d

    def get_eq_root(self, order=1):
        if order==1:
            x = (-self.b + self.d ** (1/2.0)) / 2*self.a
        else:
            x = (-self.b - self.d ** (1/2.0)) / 2*self.a
        return x

def quadratic_eval(a, b, c):
    variables = {}

    quad = Quadratic(a, b, c)
    quad.calc_discrim()
    d = quad.get_discrim()
    variables.update(d=d)
    if d >= 0:
        x1 = quad.get_eq_root()
        x2 = quad.get_eq_root(order=2)
        variables.update(x1=x1, x2=x2)

    return variables
