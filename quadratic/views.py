from django.shortcuts import render

# Create your views here.

from utils.utils_qe import quadratic_equ

def quadratic_results(request):
    # Call function quadratic_equ, which considers quadratic equation
    dict_quadr = quadratic_equ(request.GET['a'], request.GET['b'], request.GET['c'])

    return render(request, 'quadratic/index_quadratic.html',

        {'a': dict_quadr['a'], 'b': dict_quadr['b'], 'c': dict_quadr['c'],
        'a_native': request.GET['a'], 'b_native': request.GET['b'], 'c_native': request.GET['c'],
        'd': dict_quadr['d'], 'x_1': dict_quadr['x_1'], 'x_2': dict_quadr['x_2'], 'result': dict_quadr['result']}
    )
