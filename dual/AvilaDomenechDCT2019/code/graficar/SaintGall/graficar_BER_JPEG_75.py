# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def run_main():
    
    DCT_1_100 = [
        0.008065,0.008065,0.004422,0.007804,0.004683,0.008585,0.006243,0.006764,0.003642,0.004683,0.008065,0.006243,0.004683,0.008585,0.008845,0.006243,0.008845,0.005723,0.005463,0.005463,0.001821,0.005723,0.005983,0.004162,0.008325,0.008845,0.007544,0.007024,0.005463,0.006504,0.005463,0.004162,0.005463,0.006243,0.005723,0.004683,0.007544,0.007024,0.005983,0.007804,0.007544,0.004683,0.001821,0.006504,0.007024,0.005723,0.009625,0.004943,0.003902,0.009625,0.005203,0.005723,0.003382,0.005723,0.006243,0.007024,0.004162,0.008325,0.006243,0.006764,
    ]

    # ok
    Krawtchouk_19_128 = [
        0.021072,0.018991,0.017430,0.012747,0.019251,0.020031,0.019251,0.013528,0.016389,0.017690,0.019251,0.017690,0.016129,0.018210,0.013788,0.016129,0.018470,0.018470,0.017170,0.016649,0.017170,0.018470,0.016909,0.019771,0.018210,0.015088,0.017430,0.018730,0.015349,0.018730,0.016129,0.015869,0.014308,0.015609,0.017430,0.012487,0.021332,0.023153,0.018470,0.017690,0.018730,0.021592,0.017950,0.016649,0.019771,0.021852,0.017430,0.016649,0.020031,0.020812,0.012487,0.016649,0.021332,0.014828,0.018730,0.018730,0.019251,0.015609,0.017690,0.016909
    ]

    data = [DCT_1_100, Krawtchouk_19_128]

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
    ax1.set_title('Saint Gall database (60 images)')
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