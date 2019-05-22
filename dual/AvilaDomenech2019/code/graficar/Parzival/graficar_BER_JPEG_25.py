# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def run_main():
    shivani2017 = [
        0.097034,0.087409,0.082726,0.089230,0.080385,0.060614,0.093132,0.092352,0.086629,0.080385,0.088189,0.066337,0.096514,0.089750,0.091571,0.083247,0.071540,0.091051,0.071540,0.082986,0.080645,0.069199,0.064776,0.063476,0.073361,0.080645,0.096774,0.081686,0.080905,0.082726,0.082206,0.079084,0.067638,0.086629,0.059834,0.084547,0.078304,0.088710,0.081426,0.084547,0.082726,0.098075,0.082466,0.088450,0.084287,0.087409,0.040323,
    ]

    liu2018 = [
        0.097034,0.087409,0.082726,0.089230,0.080385,0.060614,0.093132,0.092352,0.086629,0.080385,0.088189,0.066337,0.096514,0.089750,0.091571,0.083247,0.071540,0.091051,0.071540,0.082986,0.080645,0.069199,0.064776,0.063476,0.073361,0.080645,0.096774,0.081686,0.080905,0.082726,0.082206,0.079084,0.067638,0.086629,0.059834,0.084547,0.078304,0.088710,0.081426,0.084547,0.082726,0.098075,0.082466,0.088450,0.084287,0.087409,0.040323
    ]

    avila2018 = [
        0.097034,0.087409,0.082726,0.089230,0.080385,0.060614,0.093132,0.092352,0.086629,0.080385,0.088189,0.066337,0.096514,0.089750,0.091571,0.083247,0.071540,0.091051,0.071540,0.082986,0.080645,0.069199,0.064776,0.063476,0.073361,0.080645,0.096774,0.081686,0.080905,0.082726,0.082206,0.079084,0.067638,0.086629,0.059834,0.084547,0.078304,0.088710,0.081426,0.084547,0.082726,0.098075,0.082466,0.088450,0.084287,0.087409,0.040323
    ]

    proposed = [
        0.097034,0.087409,0.082726,0.089230,0.080385,0.060614,0.093132,0.092352,0.086629,0.080385,0.088189,0.066337,0.096514,0.089750,0.091571,0.083247,0.071540,0.091051,0.071540,0.082986,0.080645,0.069199,0.064776,0.063476,0.073361,0.080645,0.096774,0.081686,0.080905,0.082726,0.082206,0.079084,0.067638,0.086629,0.059834,0.084547,0.078304,0.088710,0.081426,0.084547,0.082726,0.098075,0.082466,0.088450,0.084287,0.087409,0.040323
    ]

    data = [shivani2017, liu2018, avila2018, proposed]

    fig, ax1 = plt.subplots(figsize=(6, 6))
    fig.canvas.set_window_title('BER')
    fig.subplots_adjust(left=0.11, right=0.95, top=0.95, bottom=0.05)

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
    ax1.set_title('Parzival database (47 images)')
    ax1.set_xlabel('Schemes')
    ax1.set_ylabel('BER')

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