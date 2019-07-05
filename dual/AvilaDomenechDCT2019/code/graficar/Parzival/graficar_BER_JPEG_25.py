# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def run_main():
    # ok
    DCT_1_100 = [
        0.028356,0.031478,0.025234,0.027315,0.028356,0.015349,0.030437,0.031998,0.033559,0.027315,0.028096,0.023153,0.026535,0.033819,0.031738,0.032778,0.023673,0.032778,0.027055,0.025754,0.030177,0.023413,0.014048,0.016129,0.020812,0.029657,0.031478,0.025754,0.026275,0.030697,0.031478,0.030697,0.020812,0.027055,0.022373,0.027315,0.029136,0.022893,0.027575,0.023153,0.032778,0.033559,0.024454,0.030177,0.027836,0.030177,0.004422,
    ]

    # ok
    proposed = [
        0.086368,0.076223,0.079865,0.084807,0.082466,0.055411,0.096514,0.092872,0.082466,0.080125,0.076743,0.086629,0.086889,0.082986,0.080645,0.059313,0.072320,0.093392,0.065297,0.090010,0.085068,0.085848,0.085328,0.084287,0.094433,0.068939,0.086629,0.085588,0.084287,0.092872,0.081946,0.066597,0.037461,0.087669,0.085328,0.085588,0.079865,0.084287,0.092092,0.078564,0.080385,0.079344,0.088710,0.087669,0.069719,0.091051,0.091051
    ]

    data = [DCT_1_100, proposed]

    fig, ax1 = plt.subplots(figsize=(6, 6))
    fig.canvas.set_window_title('BER')
    fig.subplots_adjust(left=0.11, right=0.95, top=0.95, bottom=0.15)

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