# -*- coding: utf-8 -*-
# import utils
#
#Решение квадратного уравнения

def quadratic_equel (par1, par2, par3):
    dict_result = {'a':'none', 'b':'none', 'c':'none', 'd':'none', 'x_1':'none', 'x_2':'none', 'result':'none'}
    #Определение коефициентов
    dict_result['a'] = utils.check_param(par1)
    dict_result['b'] = utils.check_param(par2)
    dict_result['c'] = utils.check_param(par3)
    if dict_result['a'] == 0:
        dict_result['a'] = 'first param is zero'
    #Решение квадратного уравнения
    if type(dict_result['a']) is int and type(dict_result['b']) is int and type(dict_result['c']) is int:
        dict_result['d'] = utils.get_discr(dict_result['a'], dict_result['b'], dict_result['c'])
        if dict_result['d'] <0:
            dict_result['result'] = 'Disct less zero'
        elif dict_result['d']==0:
            dict_result['x_1'] = utils.get_eq_root(dict_result['a'], dict_result['b'], dict_result['d'])
            dict_result['x_2'] = dict_result['x_1']
            dict_result['result'] = 'One root'
        else:
            dict_result['x_1'] = utils.get_eq_root(dict_result['a'], dict_result['b'], dict_result['d'])
            dict_result['x_2'] = utils.get_eq_root(dict_result['a'], dict_result['b'], dict_result['d'], 0)
            dict_result['result'] = 'Two roots'
    return dict_result

