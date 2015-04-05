from django.shortcuts import render

from methods import methods

def quadratic_results(request):
	
	res = methods.q_calc(request.GET['a'], request.GET['b'], request.GET['c'])

	return render(request, 'quadratic/index_q.html', 
		{'a':res['a'], 'b':res['b'], 'c':res['c'],
        'a_get':request.GET['a'], 'b_get':request.GET['b'], 'c_get':request.GET['c'],
        'd':res['d'], 'x1':res['x1'], 'x2':res['x2']})