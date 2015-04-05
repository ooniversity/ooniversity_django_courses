from django.shortcuts import render
from quadratic import resolver

def results(request):
	a = request.GET['a']
	b = request.GET['b']
	c = request.GET['c']
	a_result = resolver.check_value(a)[1]
	b_result = resolver.check_value(b)[1]
	c_result = resolver.check_value(c)[1]
	answer = resolver.resolve(a, b, c)
	result = answer['result']
	discr = answer['discr']
	return render(request, "results.html",{'a': a, 'b': b, 'c': c,'a_result': a_result, 'b_result': b_result, 'c_result': c_result, 'result': result, 'd':discr})