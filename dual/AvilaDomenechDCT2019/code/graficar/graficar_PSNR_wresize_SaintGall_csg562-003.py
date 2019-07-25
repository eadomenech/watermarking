# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def run_main():

    fig, ax1 = plt.subplots(figsize=(6, 4))
    fig.canvas.set_window_title('PSNR')
    fig.subplots_adjust(left=0.1, right=0.95, top=0.93, bottom=0.1)

    # Add a horizontal grid to the plot, but make it very light in color
    # so we can use it for reading data values but not be distracting
    ax1.yaxis.grid(
        True, linestyle='-', which='major', color='lightgrey',
        alpha=0.5)

    # Hide these grid behind plot objects
    ax1.set_axisbelow(True)
    ax1.set_title('Saint Gall database (csg562-003.jpg)')
    ax1.set_xlabel('Watermark size')
    ax1.set_ylabel('PSNR')
    
    plt.rc('font', size = 12)

    # PSNR    
    # ok
    plt.plot(
        (39.132369,39.150086,39.147547,39.164151,39.139622,39.182748),
        label = '[15]', color='darkkhaki')
    # ok
    plt.plot(
        (32.855299,32.854757,32.850704,32.839909,32.794834,32.620050),
        label = '[10] k=0.4', color='green')
    # ok
    plt.plot(
        (56.851671,55.636493,53.089555,48.743750,43.323817,37.134046,),
        label = 'DCT-RW + FW', color='blue')
    # ok
    plt.plot(
        (56.646316,55.110089,53.651019,47.838714,42.110737,36.161967),
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