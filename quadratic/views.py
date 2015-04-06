from django.http import HttpResponse
from django.shortcuts import render

from quadratic.models import *

def parameters(request):

    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']

    zero_a = find_zero(a)

    except_a = find_exception(a)
    except_b = find_exception(b)
    except_c = find_exception(c)

    d = get_discr(a, b, c)

    eq_root = get_eq_root(a, b, d)

    return render (request, 'results.html',
                   {'a':a, 'b': b, 'c':c, 'd':d, 'zero_a': zero_a,
                    'except_a':except_a, 'except_b':except_b, 'except_c':except_c,
                    'eq_root': eq_root}  )


