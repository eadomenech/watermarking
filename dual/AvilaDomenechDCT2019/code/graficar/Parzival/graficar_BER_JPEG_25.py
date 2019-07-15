# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def run_main():
    
    # ok, DCT-RW
    DCT_RW_1_100 = [
        0.034860,0.027836,0.026015,0.024974,0.033039,0.029657,0.038241,0.028096,0.036941,0.004943,0.026015,0.036160,0.026795,0.031217,0.034079,0.034599,0.034599,0.029657,0.026535,0.027836,0.035380,0.031478,0.036420,0.033299,0.021592,0.031998,0.031738,0.028876,0.029917,0.024714,0.016909,0.025494,0.035380,0.018470,0.033039,0.031478,0.029657,0.021592,0.028356,0.036420,0.028356,0.031217,0.040323,0.035380,0.032518,0.029657,0.035120,
    ]
    
    # ok, DCT-RFW
    DCT_RFW_1_100 = [
        0.028356,0.032778,0.025754,0.024974,0.030437,0.031738,0.040062,0.027055,0.035900,0.009625,0.030437,0.030437,0.030177,0.030437,0.028616,0.028096,0.030957,0.028876,0.028616,0.027836,0.028096,0.031217,0.030697,0.031738,0.019251,0.029657,0.032258,0.029917,0.029657,0.023933,0.015349,0.026275,0.030957,0.021332,0.030957,0.034339,0.031998,0.021592,0.024714,0.033299,0.023413,0.028096,0.037721,0.034599,0.038241,0.033819,0.034599,
    ]

    # ok, DKT_RW
    DKT_RW_19_128 = [
        0.081426,0.086368,0.079605,0.064776,0.082206,0.082726,0.085848,0.085588,0.099376,0.038502,0.083767,0.084807,0.086889,0.086889,0.093392,0.077523,0.091051,0.082726,0.083247,0.084287,0.099636,0.079344,0.092612,0.096514,0.052029,0.078304,0.092612,0.086889,0.086108,0.064776,0.072060,0.068678,0.089750,0.061655,0.092872,0.088189,0.073101,0.081946,0.073881,0.075442,0.091831,0.078824,0.082466,0.087409,0.086368,0.075442,0.099376,
    ]

    # ok, DKT_RFW
    DKT_RFW_19_128 = [
        0.080645,0.082206,0.074142,0.068158,0.081426,0.086889,0.096774,0.079344,0.097294,0.040323,0.083767,0.087929,0.087669,0.085068,0.085848,0.090531,0.093132,0.081165,0.085588,0.087929,0.082466,0.086629,0.085848,0.095994,0.059313,0.081426,0.091051,0.083507,0.091571,0.061915,0.065036,0.074402,0.079865,0.052549,0.086629,0.078824,0.085328,0.068678,0.074142,0.078304,0.087669,0.079344,0.086629,0.085068,0.090531,0.081165,0.095473,
    ]

    data = [DCT_RW_1_100, DCT_RFW_1_100, DKT_RW_19_128, DKT_RFW_19_128]

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
    boxColors = [ '#ade1f9', 'blue', '#c586c0', 'red']
    for i in range(len(boxColors)):
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
            'DCT-RW', 'DCT-RW + FW', 'Krawtchouk-RW',
            'Krawtchouk-RW + FW'
        ],
        rotation=-20, fontsize=12)
    plt.show()


if __name__ == "__main__":
    run_main()