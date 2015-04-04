from django.shortcuts import render
from django.http import HttpResponse

def quadratic_results(request):
    dict = {'a': '', 'b': '', 'c': ''}
    for i in dict:
        if i in request.GET:
            dict[i] = request.GET[i]
    if dict['a'] != 0:
        for i in dict:
            if dict[i] != '' and dict[i].replace('-'.'').isdigit():
                discr = int(dict[b]) ** 2 - 4 * int(dict[a]) * int(dict[c])
                dict['discr'] = discr
                if discr == 0:
                    x1 = x2 = -dict['b'] / 2*dict['a']
                elif discr > 0:
                    x1 = (-dict['b'] + discr ** 0.5) / (2 * dict['a'])
                    x2 = (-dict['b'] - discr ** 0.5) / (2 * dict['a'])
                dict['x1'] = x1
                dict['x2'] = x2
        
    return render(request, 'quadratic.html', dict)