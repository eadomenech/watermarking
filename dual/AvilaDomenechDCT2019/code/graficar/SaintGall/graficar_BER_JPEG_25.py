# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def run_main():

    # ok, DCT-RW
    DCT_RW_1_100 = [
        0.007804,0.007544,0.007284,0.007284,0.009886,0.008845,0.007804,0.009365,0.005983,0.005203,0.009886,0.005203,0.009625,0.007544,0.009105,0.006764,0.008585,0.005983,0.007544,0.006504,0.002341,0.008845,0.005983,0.006243,0.008065,0.005203,0.009365,0.008585,0.006504,0.008585,0.008585,0.009105,0.007024,0.008065,0.006504,0.007544,0.009625,0.006504,0.005983,0.010146,0.007544,0.007544,0.004162,0.005203,0.009625,0.004943,0.009365,0.008065,0.006764,0.007284,0.010146,0.008585,0.006243,0.005983,0.010406,0.008845,0.005723,0.008065,0.005463,0.004422,
    ]
    
    # ok, DCT-RFW
    DCT_RFW_1_100 = [
        0.011967,0.011186,0.006504,0.008845,0.008585,0.008065,0.007284,0.006764,0.008325,0.005463,0.009105,0.005723,0.008325,0.006243,0.010406,0.007804,0.009625,0.008585,0.008845,0.008845,0.003642,0.008065,0.005463,0.007544,0.008325,0.006764,0.008325,0.007284,0.008845,0.008325,0.010406,0.010146,0.007284,0.005463,0.009886,0.005723,0.009365,0.007544,0.008325,0.007544,0.008065,0.007284,0.004683,0.007284,0.010146,0.004422,0.007804,0.010146,0.007284,0.005723,0.007284,0.007804,0.008065,0.012227,0.009625,0.007284,0.009886,0.008585,0.005463,0.005203,
    ]

    # ok, DKT_RW
    DKT_RW_19_128 = [
        0.015609,0.024194,0.015869,0.018210,0.020291,0.017690,0.014568,0.017430,0.017430,0.014568,0.020812,0.015088,0.016909,0.020552,0.020291,0.020812,0.019511,0.019511,0.015349,0.018210,0.016649,0.016649,0.015869,0.017170,0.021332,0.017430,0.022112,0.020812,0.014828,0.018991,0.019511,0.025234,0.016389,0.014308,0.020812,0.016129,0.021852,0.024194,0.015609,0.017170,0.023673,0.020291,0.013267,0.019511,0.021332,0.015349,0.024454,0.020291,0.018991,0.017950,0.018991,0.016649,0.015869,0.019251,0.022373,0.018991,0.013267,0.017170,0.016909,0.017170,
    ]

    # ok, DKT_RFW
    DKT_RFW_19_128 = [
        0.021332,0.019511,0.018991,0.013528,0.020291,0.020031,0.020291,0.014828,0.016909,0.018470,0.020031,0.018470,0.016389,0.018470,0.014828,0.016389,0.019511,0.020031,0.017950,0.017430,0.018210,0.019771,0.017430,0.021332,0.018730,0.016389,0.017430,0.021332,0.016129,0.019251,0.016129,0.016129,0.014568,0.015609,0.018470,0.012487,0.022112,0.023673,0.019511,0.018470,0.019771,0.022112,0.018730,0.017170,0.020812,0.022112,0.018210,0.018210,0.020291,0.021852,0.013528,0.017950,0.021852,0.015088,0.019251,0.019251,0.019771,0.016389,0.019511,0.017430
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
    ax1.set_title('Saint Gall database (60 images)')
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