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
    frec = None
    for clase in lista:
        if not frec == clase[:2]:
            frec = clase[:2]
            dic_cantidades[frec] = 0
        paths = glob.glob('join/' + clase + '/*.png')
        dic_cantidades[frec] += len(paths)
    
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.arange(0, 8, 1)
    y = np.arange(0, 8, 1)
    array = np.zeros((8,8))
    for f in range(1, 63):
        # Posicion rererente al zigzag
        (posX, posY) = get_indice(f)
        array[posX, posY] = dic_cantidades[convert(f)]
    plt.imshow(array)
    plt.colorbar(orientation='vertical')
    plt.show()


    


if __name__ == '__main__':
    main()
