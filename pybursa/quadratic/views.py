from django.shortcuts import render

def quadratic(request):
    return render(request, 'quadratic.html')

def result(request):

    def get_param(param):
        try:
            return request.GET[param]
        except:
            return ''

    a = get_param('a')
    b = get_param('b')
    c = get_param('c')

    def check_param(param):
        status = ''
        if param == '':
            status = "Koeffitsient ne opredelen"
        elif not param.replace('-','',1).isdigit():
            status = "Koeffitsient ne tseloe chislo"
        print param, status
        return status


    a_status = check_param(a)
    if a_status == '':
        a = int(a)
    
    b_status = check_param(b)
    if b_status == '':
        b = int(b)
    
    c_status = check_param(c)
    if c_status == '':
        c = int(c)

    d_status = ''
    d = 0
    


    if a == 0:
        a_status = "Koeffitsient pri pervom slagaemom uravneniya ne mozhet byit ravnyim nulyu"

    elif a_status != 0 and b_status != "Koeffitsient ne tseloe chislo" and c_status != "Koeffitsient ne tseloe chislo":

        d = float(b*b   - 4*a*c)

        if d > 0:
            x1 = float((-b + d**0.5) / 2*a)
            x2 = float((-b - d**0.5) / 2*a)
            d_status = "Kvadratnoe uravnenie imeet 2 deystvitelnyih kornya: x1 = %s, x2 = %s" % (x1,x2)
        elif d == 0:
            x1 = x2 = float(- b / 2*a)
            d_status = "Diskriminant raven nulyu, kvadratnoe uravnenie imeet odin deystvitelnyiy koren: x1 = x2 = %s" % x1
        else:
            d_status = "Diskriminant menshe nulya, kvadratnoe uravnenie ne imeet deystvitelnyih korney"



    return render(request, 'results.html', { 'a':[a,a_status], 'b':[b,b_status], 'c':[c,c_status], 'd':[d, d_status]}  )