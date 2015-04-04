from django.shortcuts import render

def quadratic_results(request):
	data = {"a":request.GET['a'], "b":request.GET['b'], "c":request.GET['c']}
	discr = None
	roots = []
	flag_eq1 = True
	flag_eq2 = True
	flag_eq3 = True
	try: 
		data["a"] = int(request.GET['a'])
	except ValueError:
		flag_eq1 = False
	try: 
		data["b"] = int(request.GET['b'])
	except ValueError:
		flag_eq2 = False
	try: 
		data["c"] = int(request.GET['c'])
	except ValueError:
		flag_eq3 =False
	if flag_eq1 and flag_eq2 and flag_eq3:
		roots, discr = get_roots(data['a'], data['b'], data['c'])
	print roots	

	parametrs = {'a':data['a'], 'b':data['b'], 'c': data['c'], 'discr' : discr, 'roots' : roots, 
	             'flag1' : flag_eq1, 'flag2' : flag_eq2, 'flag3' : flag_eq3}

	return render(request, 'results.html', parametrs)

def get_discr(a,b,c):
	d = None
	if a!= 0:
		d = b**2 - 4*a*c
	return d

def get_roots(a, b, c):
	roots = []
	discr = get_discr(a, b, c)
	if discr >= 0 and a != 0:
		roots = [(-b + discr**(1/2.0))/(2*a), (-b - discr**(1/2.0))/(2*a)]
	return roots, discr	

