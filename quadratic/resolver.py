def check_value(value):
    result=''
    if value:
        try:
        	int(value)
        	result = [True ,'']
        except ValueError:
            result = [False, '\nCoefficient is not integer']
    else:
        result = [False , "\nCoefficient is empty"]
    return result

def discr(a, b, c):
    return b**2 - 4*a*c

def check_discr(d):
    result = ''
    if d < 0:
        result = [False, 'Discriminant less then 0, equation has no solutions ']
    elif d > 0:
        result = [True, 'Equation has two solutions ']
    else:
        result = [True, 'Equation has one solutions ']
    return result

def find_solution(a, b, d):
    s = []
    s.append(-b + d**(1/2.0)/2*a)
    s.append(-b - d**(1/2.0)/2*a)
    return s

def resolve(a=None, b=None, c=None):
    solution = {'result':'', 'discr':''}
    if not(check_value(a)[0] and check_value(b)[0] and check_value(c)[0]):
        return solution
    a = int(a)
    b = int(b)
    c = int(c)
    d = discr(a, b, c)
    solution['discr'] = 'Discriminant= '+ str(d)
    if check_discr(d)[0]:
        if d == 0:
            solution['result'] = solution['result'] + check_discr(d)[1] + "x1=x2= " + str(-b/2*a)
        else:
            s = find_solution(a, b, d)
            solution['result'] = solution['result']+ check_discr(d)[1] + "x1 = " + str(s[0]) + " x2 = " + str(s[1])
    else:
        solution['result'] = solution['result'] + check_discr(d)[1]
    return solution


print resolve(1, 10, 3)