# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def run_main():
    
    DCT_1_100 = [
        47.612305,47.159009,48.162222,47.543687,47.986418,47.502569,47.689146,47.807145,47.969431,48.310078,47.350608,47.856839,47.856492,47.553862,47.598500,47.618940,47.319838,47.634566,48.093747,48.100511,48.577917,47.831267,48.068906,47.945063,47.284070,47.712451,47.548653,47.759068,47.848484,47.812204,47.893433,47.584011,48.216134,47.677009,47.498879,47.667732,47.421944,47.271808,47.353212,47.369984,47.482419,48.117960,48.736260,47.425148,47.599467,47.818650,47.201597,47.560030,47.665555,47.489818,47.447197,47.512005,48.088265,47.684365,47.480740,47.636622,48.126484,47.544574,47.789327,48.046068,
    ]

    # ok
    Krawtchouk_19_128 = [
        47.878285,47.853420,48.046414,47.907034,47.939477,47.735455,47.935446,47.854021,48.042707,48.057450,47.922732,47.890937,48.039144,47.941093,47.888722,48.052789,47.899229,47.838873,47.879789,48.114369,47.995086,47.864612,47.945915,48.057047,47.821185,47.923829,47.894378,47.893424,48.005227,47.908769,47.802983,47.909813,47.961407,48.023033,47.846028,47.950894,47.825479,47.810997,47.854622,47.887811,47.953857,48.050256,48.069505,47.921089,47.801456,47.899878,47.760746,47.884980,47.952854,47.921674,47.749830,47.810677,47.889319,47.923516,47.834536,47.942949,47.874924,47.914484,47.852892,47.995507
    ]

    data = [
        DCT_1_100, Krawtchouk_19_128]

    fig, ax1 = plt.subplots(figsize=(6, 6))
    fig.canvas.set_window_title('PSNR')
    fig.subplots_adjust(left=0.1, right=0.95, top=0.95, bottom=0.15)

    bp = ax1.boxplot(data, notch=0, sym='+', vert=1, whis=1.5)
    plt.setp(bp['boxes'], color='blue')
    plt.setp(bp['whiskers'], color='black')
    plt.setp(bp['fliers'], marker='+', color='blue')

    # Add a horizontal grid to the plot, but make it very light in color
    # so we can use it for reading data values but not be distracting
    ax1.yaxis.grid(
        True, linestyle='-', which='major', color='lightgrey',
        alpha=0.5)

    # Hide these grid behind plot objects
    ax1.set_axisbelow(True)
    ax1.set_title('Saint Gall database (60 images)')
    ax1.set_xlabel('Schemes')
    ax1.set_ylabel('PSNR')

    # Now fill the boxes with desired colors
    numDists = 2
    boxColors = ['blue', 'red']
    for i in range(numDists):
        box = bp['boxes'][i]
        boxX = []
        boxY = []
        for j in range(5):
            boxX.append(box.get_xdata()[j])
            boxY.append(box.get_ydata()[j])
        boxCoords = np.column_stack([boxX, boxY])
        boxPolygon = Polygon(boxCoords, facecolor=boxColors[i])
        ax1.add_patch(boxPolygon)
        # Now draw the median lines back over what we just filled in
        med = bp['medians'][i]
        # Finally, overplot the sample averages, with horizontal alignment in the center of each box
        ax1.plot([np.average(med.get_xdata())], [np.average(data[i])],
                color='w', marker='*', markeredgecolor='k')

    ax1.set_xticklabels(
        [
            'DCT (1, 100)', 'Krawtchouk (19, 128)'
        ],
        rotation=-30, fontsize=12)
    plt.show()


if __name__ == "__main__":
    run_main()