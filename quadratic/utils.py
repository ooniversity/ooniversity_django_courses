
class QuadraticEquation(object):
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	def calc_discr(self):
		self.d = self.b ** 2 - 4 * self.a * self.c

	def  get_discr(self):
		self.d = self.b ** 2 - 4 * self.a * self.c
		return self.d

	def get_eq_root(self, order=1):
		if order == 1:
			x = (-self.b + self.d ** (1/2.0)) / 2 * self.a
		else:
			x = (-self.b - self.d ** (1/2.0)) / 2 * self.a
		return x