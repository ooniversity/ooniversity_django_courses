from django.http import HttpResponse

from quadratic.models import ReportAnError, ResultsCalc
from quadratic.utils import QuadraticEquation


def quadratic_results(request):
	a = request.GET['a']
	b = int(a)
	print type(b)
	return HttpResponse('Whots up')

