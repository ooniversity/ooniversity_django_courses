from django.shortcuts import render

def quadratic_results(request, a, b, c):
	if a.isdigit():
		if b.isdigit():
			if c.isdigit():
				a = int(a)
				print a
				b = int(b)
				print b
				c = int(c)
				print c
				d = b ** 2 - 4 * a * c
				print d
				if d < 0:
					roots = "Discrimin < 0"
				elif d == 0:
					x1 = -b / 2 * a
					roots = "x1 =  %d" % x1 
				else:
					x1 = (-b + d ** (1/2.0)) / (2 * a)
					x2 = (-b - d ** (1/2.0)) / (2 * a)
					roots = "x1 = %d, x2 = %d" % (x1,x2)
				"""elif c == None :
				c_str = "koef is None"
			else :
				c_str = "koef not int"
		elif b == None :
			b_str = "koef is None"
		else :
			b_str = "koef not int"
	elif a == None :
		a_str = "koef is None"
	else :
		a_str = "koef not int"""
	return render(request, "quadratic_results.html")


