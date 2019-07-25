# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def run_main():
    # Nos ponemos en modo interactivo
    # plt.ion()
    
    # Dividimos la ventana en una fila y dos
    # columnas y dibujamos el primer gráfico

    plt.rc('font', size = 12)

    # Without noise
    plt.subplot(2,2,1)

    plt.ylabel('BER')
    plt.xlabel('Watermark size')
    
    # ok
    plt.plot(
        (0.515625,0.312500,0.405273,0.428223,0.415710,0.428802),
        label = '[15]', color='darkkhaki')
    # ok
    plt.plot(
        (0.437500,0.308594,0.417969,0.390625,0.399963,0.401199),
        label = '[10] k=0.4', color='green')
    # falta
    plt.plot(
        (0.015625,0.363281,0.286133,0.190674,0.096558,0.053207,),
        label = 'DCT-RW + FW', color='blue')
    # ok
    plt.plot(
        (0.015625,0.367188,0.284180,0.196533,0.104797,0.060440),
        label = 'Krawtchouk-RW + FW', color='red')
    
    # Colocamos las etiquetas para cada distribución
    plt.xticks(
        [0, 1, 2, 3, 4, 5],
        ['8x8', '16x16', '32x32', '64x64', '128x128', '256x256'],
        size = 'small', color = 'k', rotation=0)

    plt.legend(loc = 0)

    # BER JPEG75
    plt.subplot(2,2,2)

    plt.ylabel('BER')
    plt.xlabel('Watermark size')
    
    # ok
    plt.plot(
        (0.515625,0.371094,0.438477,0.455078,0.449036,0.453812),
        label = '[15]', color='darkkhaki')
    # ok
    plt.plot(
        (0.406250,0.261719,0.342773,0.330566,0.329102,0.312820),
        label = '[10] k=0.4', color='green')
    # ok
    plt.plot(
        (0.015625,0.363281,0.286133,0.190674,0.096558,0.053207,),
        label = 'DCT-RW + FW', color='blue')
    # ok
    plt.plot(
        (0.015625,0.367188,0.284180,0.196533,0.104797,0.060440,),
        label = 'Krawtchouk-RW + FW', color='red')

    # Colocamos las etiquetas para cada distribución
    plt.xticks(
        [0, 1, 2, 3, 4, 5],
        ['8x8', '16x16', '32x32', '64x64', '128x128', '256x256'],
        size = 'small', color = 'k', rotation=0)

    plt.legend(loc = 0)

    # BER JPEG50
    plt.subplot(2,2,3)

    plt.ylabel('BER')
    plt.xlabel('Watermark size')
    
    # ok
    plt.plot(
        (0.500000,0.402344,0.443359,0.466064,0.455688,0.454941),
        label = '[15]', color='darkkhaki')
    # ok
    plt.plot(
        (0.375000,0.296875,0.361328,0.349365,0.345642,0.327682),
        label = '[10] k=0.4', color='green')
    # ok
    plt.plot(
        (0.015625,0.363281,0.286133,0.190674,0.096558,0.053207,),
        label = 'DCT-RW + FW', color='blue')
    # ok
    plt.plot(
        (0.015625,0.367188,0.284180,0.196533,0.104797,0.060440,),
        label = 'Krawtchouk-RW + FW', color='red')

    # Colocamos las etiquetas para cada distribución
    plt.xticks(
        [0, 1, 2, 3, 4, 5],
        ['8x8', '16x16', '32x32', '64x64', '128x128', '256x256'],
        size = 'small', color = 'k', rotation=0)

    plt.legend(loc = 0)

    # BER JPEG25
    plt.subplot(2,2,4)

    plt.ylabel('BER')
    plt.xlabel('Watermark size')
    
    # ok
    plt.plot(
        (0.406250,0.335938,0.411133,0.414307,0.412109,0.403336),
        label = '[15]', color='darkkhaki')
    # ok
    plt.plot(
        (0.468750,0.304688,0.399414,0.386963,0.394348,0.378708),
        label = '[10] k=0.4', color='green')
    # ok
    plt.plot(
        (0.015625,0.363281,0.286133,0.191162,0.096619,0.053421,),
        label = 'DCT-RW + FW', color='blue')
    # ok
    plt.plot(
        (0.015625,0.367188,0.283203,0.197266,0.105774,0.061066),
        label = 'Krawtchouk-RW + FW', color='red')

    # Colocamos las etiquetas para cada distribución
    plt.xticks(
        [0, 1, 2, 3, 4, 5],
        ['8x8', '16x16', '32x32', '64x64', '128x128', '256x256'],
        size = 'small', color = 'k', rotation=0)

    plt.legend(loc = 0)    

    plt.show()


if __name__ == "__main__":
    run_main()