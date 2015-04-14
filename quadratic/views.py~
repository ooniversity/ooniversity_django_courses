from django.shortcuts import render


def quadratic_results(request):

    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')

    l1 = [a, b, c, 0]
    i = 0

    for item in l1:
        if l1[i] == '':
            l1[i] = 'No data input'
        elif l1[i] == None:
            return render(request, 'get_items.html')
        else:
            try:
                l1[i] = int(item)
            except ValueError:
                l1[i] = 'Input not integer'
        i += 1

    if 'No data input' in l1:
        return render(request, 'get_items.html', {'a': l1[0], 'b': l1[1], 'c': l1[2]})
    if 'Input not integer' in l1:
        return render(request, 'get_items.html', {'a': l1[0], 'b': l1[1], 'c': l1[2]})
    if l1[0] == 0:
        l1[0] = 'First statment cannot be Zero'
        return render(request, 'get_items.html', {'a': l1[0], 'b': l1[1], 'c': l1[2]})

    l1[3] = l1[1]**2 - 4*l1[0]*l1[2]

    if l1[3] > 0:
        import math
        x1 = (-l1[1] + math.sqrt(l1[3])) / (2*l1[0])
        x2 = (-l1[1] - math.sqrt(l1[3])) / (2*l1[0])
        disc = 'Discreminant is ' + str(l1[3])
        roots = 'Quadratic statment has 2 actual roots x1 = ' + str(x1) + ' x2 = ' + str(x2)
        return render(request, 'get_items.html', {'a': l1[0], 'b': l1[1], 'c': l1[2], 'd': disc, 'roots': roots})
    elif l1[3] == 0:
        x1 = -l1[1]/(2*l1[0])
        disc = 'Discreminant is ' + str(l1[3])
        roots = 'Discreminant is Zero and have only one actual root x1 = x2 = ' + str(x1)
        return render(request, 'get_items.html', {'a': l1[0], 'b': l1[1], 'c': l1[2], 'd': disc, 'roots': roots})
    else:
        disc = 'Discreminant is ' + str(l1[3])
        roots = 'Discreminant is less than Zero and doesnt have actual roots'
        return render(request, 'get_items.html', {'a': l1[0], 'b': l1[1], 'c': l1[2], 'd': disc, 'roots': roots})
