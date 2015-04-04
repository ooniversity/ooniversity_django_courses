# -*- coding: utf-8 -*-
def quadratic_solver(a, b, c):
	answer = {
		'd': None,
		'title': '',
		'x': []
	}
	d = b*b - 4*a*c
	answer['d'] = d
	if d > 0:
		answer['title'] = "Квадратное уровнение имеет два действительных корня"
		answer['x'].append((b + math.sqrt(d))/2*a)
		answer['x'].append((math.sqrt(d)-b)/2*a)
	elif d == 0:
		answer['title'] = "Квадратное уровнение имеет один действительный корень"
		answer['x'].append(-b/2*a)
	else:
		answer['title'] = "Дискриминант меньше нуля, квадратное уровнение не имеет действительных решений"
	return answer