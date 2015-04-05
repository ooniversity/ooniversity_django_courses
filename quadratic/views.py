from django.shortcuts import render

from quadratic.models import ReportAnError, ResultsCalc
from quadratic.utils import QuadraticEquation


def quadratic_results(request):

	a = request.GET['a']
	b = request.GET['b']
	c = request.GET['c']

	re_a = re_b = re_c = line_1 = line_2 = None

	if a == '':
		re_a = "%s" %ReportAnError.objects.get(id=2)
	elif int(a) == 0:
		re_a = "%s" %ReportAnError.objects.get(id=1)
	elif not a.replace('-', '').isdigit():
		re_a = "%s" %ReportAnError.objects.get(id=3)

	if b == '':
		re_b = "%s" %ReportAnError.objects.get(id=2)
	elif not b.replace('-', '').isdigit():
		re_b = "%s" %ReportAnError.objects.get(id=3)

	if c == '':
		re_c = "%s" %ReportAnError.objects.get(id=2)
	elif not c.replace('-', '').isdigit():
		re_c = "%s" %ReportAnError.objects.get(id=3)	

	if re_a or re_b or re_c:
		return render(request, "result.html", {'a' : a, 're_a' : re_a, 'b' : b, 're_b' : re_b, 'c' : c, 're_c' : re_c, 'line_1' : line_1, 'line_2' : line_2})
	
	a = int(a)
	b = int(b)
	c= int(c)	

	qe = QuadraticEquation(a, b, c)
	qe.calc_discr()

	if qe.get_discr() < 0:
		line_1 = "%s %d" %(ResultsCalc.objects.get(id=1), qe.get_discr())
		line_2 = "%s" %ResultsCalc.objects.get(id=2)
		return render(request, "result.html", {'a' : a, 're_a' : re_a, 'b' : b, 're_b' : re_b, 'c' : c, 're_c' : re_c, 'line_1' : line_1, 'line_2' : line_2})
	else:
		x1 = qe.get_eq_root()
		x2 = qe.get_eq_root(order = 2)

		print type(x1), type(x2)
		if x1 == x2:
			line_1 = "%s %d" %(ResultsCalc.objects.get(id=1), qe.get_discr())
			line_2 = "%s x1 = x2 = %g" %(ResultsCalc.objects.get(id=3), x1)
			return render(request, "result.html", {'a' : a, 're_a' : re_a, 'b' : b, 're_b' : re_b, 'c' : c, 're_c' : re_c, 'line_1' : line_1, 'line_2' : line_2})
		else:
			line_1 = "%s %d" %(ResultsCalc.objects.get(id=1), qe.get_discr())
			line_2 = "%s x1 = %d x2 = %d" %(ResultsCalc.objects.get(id=4), x1, x2)
			return render(request, "result.html", {'a' : a, 're_a' : re_a, 'b' : b, 're_b' : re_b, 'c' : c, 're_c' : re_c, 'line_1' : line_1, 'line_2' : line_2})

