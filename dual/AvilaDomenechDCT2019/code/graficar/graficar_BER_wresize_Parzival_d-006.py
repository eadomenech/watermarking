# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def run_main():
    plt.rc('font', size = 12)

    # Without noise
    plt.subplot(2,2,1)

    # plt.title('Parzival database (d-006.jpg)')
    plt.ylabel('BER')
    plt.xlabel('Watermark size')
    
    plt.plot(
        (0.390625,0.371094,0.459961,0.442139,0.455200,0.474503),
        label = '[15]', color='darkkhaki')
    plt.plot(
        (0.484375,0.296875,0.389648,0.399658,0.391357,0.387939),
        label = '[10] k=0.4', color='green')
    plt.plot(
        (0.031250,0.355469,0.291016,0.200928,0.113586,0.072311,),
        label = 'DCT-RW + FW', color='blue')
    plt.plot(
        (0.078125,0.375000,0.303711,0.241943,0.163147,0.124954),
        label = 'Krawtchouk-RW + FW', color='red')
    
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
        label = '[15]', color='darkkhaki')
    plt.plot(
        (0.453125,0.183594,0.342773,0.343750,0.345581,0.333252),
        label = '[10] k=0.4', color='green')
    plt.plot(
        (0.031250,0.355469,0.291016,0.200928,0.113586,0.072311,),
        label = 'DCT-RW + FW', color='blue')
    plt.plot(
        (0.078125,0.375000,0.303711,0.241943,0.163208,0.125320),
        label = 'Krawtchouk-RW + FW', color='red')

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
        label = '[15]', color='darkkhaki')
    plt.plot(
        (0.484375,0.191406,0.340820,0.341797,0.341064,0.331589),
        label = '[10] k=0.4', color='green')
    plt.plot(
        (0.031250,0.355469,0.291016,0.200928,0.113586,0.072311,),
        label = 'DCT-RW + FW', color='blue')
    plt.plot(
        (0.078125,0.375000,0.303711,0.242188,0.163269,0.125168),
        label = 'Krawtchouk-RW + FW', color='red')

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
        label = '[15]', color='darkkhaki')
    plt.plot(
        (0.453125,0.199219,0.330078,0.337646,0.344055,0.330078),
        label = '[10] k=0.4', color='green')
    plt.plot(
        (0.031250,0.355469,0.291016,0.200928,0.113586,0.072357,),
       label = 'DCT-RW + FW', color='blue')
    plt.plot(
        (0.093750,0.375000,0.305664,0.242920,0.164368,0.127075),
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