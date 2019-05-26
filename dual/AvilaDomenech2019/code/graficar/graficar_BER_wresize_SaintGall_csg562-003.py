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

    # plt.title('Parzival database (d-006.jpg)')
    plt.ylabel('BER')
    plt.xlabel('Watermark size')
    
    plt.plot(
        (0.390625,0.371094,0.459961,0.442139,0.455200,0.474503),
        label = '[9]')
    plt.plot(
        (0.484375,0.296875,0.389648,0.399658,0.391357,0.387939),
        label = '[6] k=0.4')
    # ok
    plt.plot(
        (0.437500,0.371094,0.396484,0.398682,0.368896,0.357437),
        label = '[6] k=1.0')
    # ok
    plt.plot(
        (0.015625,0.367188,0.284180,0.196533,0.104797,0.060440),
        label = 'Proposed')
    
    # Colocamos las etiquetas para cada distribución
    plt.xticks(
        [0, 1, 2, 3, 4, 5],
        ['8x8', '16x16', '32x32', '64x64', '128x128', '256x256'],
        size = 'small', color = 'k', rotation=0)

    plt.legend(loc = 0)

    # BER JPEG75
    plt.subplot(2,2,2)

    # plt.title('Parzival database (d-006.jpg)')
    plt.ylabel('BER')
    plt.xlabel('Watermark size')
    
    plt.plot(
        (0.531250,0.476562,0.494141,0.482178,0.492004,0.493286),
        label = '[9]')
    plt.plot(
        (0.453125,0.183594,0.342773,0.343750,0.345581,0.333252),
        label = '[6] k=0.4')
    # ok
    plt.plot(
        (0.406250,0.328125,0.340820,0.333740,0.315918,0.305740),
        label = '[6] k=1.0')
    # ok
    plt.plot(
        (0.015625,0.367188,0.284180,0.196533,0.104797,0.060440,),
        label = 'Proposed')

    # Colocamos las etiquetas para cada distribución
    plt.xticks(
        [0, 1, 2, 3, 4, 5],
        ['8x8', '16x16', '32x32', '64x64', '128x128', '256x256'],
        size = 'small', color = 'k', rotation=0)

    plt.legend(loc = 0)

    # BER JPEG50
    plt.subplot(2,2,3)

    # plt.title('Parzival database (d-006.jpg)')
    plt.ylabel('BER')
    plt.xlabel('Watermark size')
    
    plt.plot(
        (0.468750,0.496094,0.488281,0.485596,0.487915,0.497620),
        label = '[9]')
    plt.plot(
        (0.484375,0.191406,0.340820,0.341797,0.341064,0.331589),
        label = '[6] k=0.4')
    # ok
    plt.plot(
        (0.421875,0.328125,0.364258,0.343262,0.331299,0.317978),
        label = '[6] k=1.0')
    # ok
    plt.plot(
        (0.015625,0.367188,0.284180,0.196533,0.104797,0.060440,),
        label = 'Proposed')

    # Colocamos las etiquetas para cada distribución
    plt.xticks(
        [0, 1, 2, 3, 4, 5],
        ['8x8', '16x16', '32x32', '64x64', '128x128', '256x256'],
        size = 'small', color = 'k', rotation=0)

    plt.legend(loc = 0)

    # BER JPEG25
    plt.subplot(2,2,4)

    # plt.title('Parzival database (d-006.jpg)')
    plt.ylabel('BER')
    plt.xlabel('Watermark size')
    
    plt.plot(
        (0.515625,0.484375,0.500000,0.489990,0.494263,0.496216),
        label = '[9]')
    plt.plot(
        (0.453125,0.199219,0.330078,0.337646,0.344055,0.330078),
        label = '[6] k=0.4')
    # ok
    plt.plot(
        (0.406250,0.308594,0.388672,0.360352,0.358521,0.342834),
        label = '[6] k=1.0')
    # ok
    plt.plot(
        (0.015625,0.367188,0.283203,0.197266,0.105774,0.061066),
        label = 'Proposed')

    # Colocamos las etiquetas para cada distribución
    plt.xticks(
        [0, 1, 2, 3, 4, 5],
        ['8x8', '16x16', '32x32', '64x64', '128x128', '256x256'],
        size = 'small', color = 'k', rotation=0)

    plt.legend(loc = 0)    

    plt.show()


if __name__ == "__main__":
    run_main()