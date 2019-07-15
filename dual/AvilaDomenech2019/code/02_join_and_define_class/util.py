# -*- coding: utf-8 -*-


'''
Genera una lista con los nombres de las clases posibles
'''
def crear_lista():
    lista = []

    for c in range(62):
        coef = c + 1
        for d in range(129):
            delta = d + 1
            lista.append(str(coef)+'_'+str(delta))
    
    return lista
