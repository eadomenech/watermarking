# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def run_main():
    shivani2017 = [
        39.412400,37.953329,39.405832,38.916522,38.439209,37.999932,38.835189,37.935623,38.755422,37.274261,38.235718,37.396278,37.745851,37.487157,37.877802,37.422671,37.066242,38.170408,37.704153,37.574749,37.589621,37.812069,37.548741,37.335278,37.162564,37.086484,37.729254,37.735927,38.254805,38.744720,37.203511,37.621834,36.762054,38.031645,36.726871,37.931698,37.911517,39.595517,38.034024,37.400031,38.340388,37.830170,38.160768,39.374882,37.688412,37.946189,37.771573,37.482753,36.664810,36.918083,37.218706,37.204875,37.825845,36.613349,36.749791,38.279079,37.347104,36.789668,36.474545,36.135333]

    liu2018 = [
        32.942211,32.482750,32.873229,32.250052,32.192542,32.289131,32.175604,32.163622,32.280870,32.387490,32.261490,32.295386,32.478652,32.299353,32.189106,32.484635,32.173200,32.682220,32.192177,32.326366,32.212692,32.401887,32.145518,32.230704,32.637898,32.307429,32.256415,32.500181,32.908275,32.394803,32.270795,32.465574,32.069685,32.199538,32.341669,32.522166,32.380163,32.472673,32.094687,32.034447,32.271921,32.487768,32.567326,32.664959,32.422300,32.170887,31.997221,32.130697,32.202558,32.075111,32.463362,32.002566,32.181643,32.185171,32.096452,32.209672,32.296958,32.123008,32.168209,31.892561
    ]

    avila2018 = [
        42.944325,43.068719,43.216445,42.818183,42.886869,43.040067,42.862763,42.873275,42.895967,42.845578,42.829701,42.859263,43.020349,42.891859,42.793530,42.828940,42.697656,42.806485,42.708147,42.954417,42.739838,42.973886,43.019405,42.963837,42.935496,42.879402,42.823496,42.921498,42.853788,42.847901,42.917794,42.893857,43.015701,42.884806,42.983556,42.820283,42.868969,43.035158,42.834006,42.918017,42.861040,42.833004,42.966341,42.885259,42.963796,42.890674,43.073579        
    ]

    proposed = [
        47.878285,47.853420,48.046414,47.907034,47.939477,47.735455,47.935446,47.854021,48.042707,48.057450,47.922732,47.890937,48.039144,47.941093,47.888722,48.052789,47.899229,47.838873,47.879789,48.114369,47.995086,47.864612,47.945915,48.057047,47.821185,47.923829,47.894378,47.893424,48.005227,47.908769,47.802983,47.909813,47.961407,48.023033,47.846028,47.950894,47.825479,47.810997,47.854622,47.887811,47.953857,48.050256,48.069505,47.921089,47.801456,47.899878,47.760746,47.884980,47.952854,47.921674,47.749830,47.810677,47.889319,47.923516,47.834536,47.942949,47.874924,47.914484,47.852892,47.995507
    ]

    data = [shivani2017, liu2018, avila2018, proposed]

    fig, ax1 = plt.subplots(figsize=(6, 6))
    fig.canvas.set_window_title('PSNR')
    fig.subplots_adjust(left=0.1, right=0.95, top=0.95, bottom=0.05)

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
    numDists = 4
    boxColors = ['darkkhaki', 'green', 'blue', 'red']
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
            '[10]', '[7]', '[2]', 'Proposed'
        ],
        rotation=0, fontsize=14)
    plt.show()


if __name__ == "__main__":
    run_main()