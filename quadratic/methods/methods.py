def get_discr(a, b, c):
    d = b**2 - 4 * a * c
    return d

def get_eq_root(a, b, d, order=1):
    if order==1:
        x = (-b + d ** (1/2.0)) / 2 * a
    else:
        x = (-b - d ** (1/2.0)) / 2 * a
    return x

def check(p):
    sign = 1
    if p.startswith('-'):
        p = p[1:]
        sign = -1
    if not p.isdigit() :
        if p=='':
            return 'error_type1'
        return 'error_type2'
    else:
        return int(p)*sign

def q_calc (a, b, c):
    result = {'a': 0, 'b': 0, 'c': 0, 'd': '', 'x1': 0, 'x2': 0}
    result['a'] = check(a)
    result['b'] = check(b)
    result['c'] = check(c)
    if result['a'] == 0:
        result['a'] = '0'
        return result

    if type(result['a']) is int and type(result['b']) is int and type(result['c']) is int:
        result['d'] = get_discr(result['a'], result['b'], result['c'])
        if result['d'] <0:
            return result
        elif result['d']==0:
            result['x1'] = get_eq_root(result['a'], result['b'], result['d'])
            result['x2'] = result['x1']
        else:
            result['x1'] = get_eq_root(result['a'], result['b'], result['d'])
            result['x2'] = get_eq_root(result['a'], result['b'], result['d'], 0)
    return result