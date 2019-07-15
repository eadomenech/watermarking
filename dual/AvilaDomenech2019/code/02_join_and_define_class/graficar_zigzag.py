# -*- coding: utf-8 -*-
# For the cluster

from PIL import Image

import os
import random
import glob
import util
import numpy as np

'''
Encargada de graficar el mapa de color teniendo en cuenta la frecuencia,
el valor delta y la cantidad de imagenes donde el optimo se obtiene con estos valores
'''
def convert(num):
    if num < 10:
        return str(num)+'_'
    return str(num)

def zigzag(n):
        indexorder = sorted(((x, y) for x in range(n) for y in range(n)), key=lambda s: (s[0]+s[1], -s[1] if (s[0]+s[1]) % 2 else s[1]))
        return {index: n for n, index in enumerate(indexorder)}

def get_indice(m):
        zarray = zigzag(8)
        px = -1
        py = -1
        n = int(len(zarray) ** 0.5 + 0.5)
        for x in range(n):
            for y in range(n):
                if zarray[(x, y)] == m:
                    px = x
                    py = y
        return (px, py)

def main():
    # Creando lista de direcciones posibles
    lista = util.crear_lista()
    # Totalizando    
    dic_cantidades = {}
    dic_cantidades['16'] = 5700
    dic_cantidades['17'] = 500
    dic_cantidades['18'] = 460
    dic_cantidades['19'] = 42240
    dic_cantidades['20'] = 450
    dic_cantidades['21'] = 10
    dic_cantidades['22'] = 620
    dic_cantidades['23'] = 5
    dic_cantidades['24'] = 220
    dic_cantidades['25'] = 5
    dic_cantidades['26'] = 560
    dic_cantidades['27'] = 2
    dic_cantidades['28'] = 450
    dic_cantidades['29'] = 230
    dic_cantidades['30'] = 84
    dic_cantidades['31'] = 80
    dic_cantidades['32'] = 89
    dic_cantidades['33'] = 3
    dic_cantidades['34'] = 650
    dic_cantidades['35'] = 2
    dic_cantidades['36'] = 3
    dic_cantidades['37'] = 2
    dic_cantidades['38'] = 30
    dic_cantidades['39'] = 1
    dic_cantidades['40'] = 23
    dic_cantidades['41'] = 3
    dic_cantidades['42'] = 2
    dic_cantidades['43'] = 1248
    dic_cantidades['44'] = 2
    dic_cantidades['45'] = 1
    dic_cantidades['46'] = 5
    dic_cantidades['47'] = 3
    dic_cantidades['48'] = 434
    
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.arange(0, 8, 1)
    y = np.arange(0, 8, 1)
    array = np.zeros((8,8))
    for f in range(16, 49):
        # Posicion rererente al zigzag
        (posX, posY) = get_indice(f)
        array[posX, posY] = dic_cantidades[convert(f)]
    plt.imshow(array)
    plt.colorbar(orientation='vertical')
    plt.show()


    


if __name__ == '__main__':
    main()
