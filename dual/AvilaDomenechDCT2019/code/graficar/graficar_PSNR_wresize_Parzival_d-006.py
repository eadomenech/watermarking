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
    ax1.set_title('Parzival database (d-006.jpg)')
    ax1.set_xlabel('Watermark size')
    ax1.set_ylabel('PSNR')
    
    plt.rc('font', size = 12)

    # PSNR    
    plt.plot(
        (31.529351,31.519621,31.502306,31.479135,31.505231,31.531263),
        label = '[9]')
    plt.plot(
        (30.166893,30.166176,30.159806,30.144635,30.077978,29.824320),
        label = '[6] k=0.4')
    plt.plot(
        (30.165325,30.160141,30.126458,30.036129,29.677881,28.460565),
        label = '[6] k=1.0')
    plt.plot(
        (
            55.473884,52.385674,50.150289,42.793328,36.985080,30.980603
        ),
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