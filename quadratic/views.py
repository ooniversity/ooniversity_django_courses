from django.shortcuts import render
from quadratic import resolver

def results(request):
	a = request.GET['a']
	b = request.GET['b']
	c = request.GET['c']
	a_result = int(resolver.check_value(a)[0])
    #b_result = resolver.check_value(b)
    #c_result = resolver.check_value(c)
    #result = resolver.resolve(a, b, c)
	return render(request, "results.html",{'a': a,'a_result': a_result})