# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def run_main():
    # ok
    shivani2017 = [
        30.563712,31.194392,30.785826,30.409946,30.451353,33.202542,30.180221,30.407400,31.035311,30.434734,31.968193,32.524636,30.483800,31.392036,30.211607,30.753252,30.678963,31.896900,31.380556,30.268878,30.351203,30.176124,30.069095,29.782338,31.402860,31.596106,31.517331,30.709524,29.935520,30.261183,30.060961,29.938812,30.137514,30.703806,30.139385,30.315976,31.398825,30.636477,30.517895,30.282455,30.457058,30.414351,30.476811,32.027260,30.384836,30.972883,30.070662
    ]

    # ok
    liu2018_k04 = [
        29.247424,29.729932,29.503719,29.173613,29.131904,29.679466,29.101913,29.253922,29.316456,29.125007,29.603383,29.880429,29.193217,29.288578,29.017481,29.199459,29.231833,29.470782,29.377425,29.144670,29.138277,28.967238,28.842931,28.748061,29.311392,29.309165,30.145597,29.330608,28.939172,29.034334,29.130543,28.891387,28.946586,29.314380,28.998285,29.139897,29.675360,29.345964,28.862683,29.094916,29.007700,29.184028,29.160143,29.560788,29.004045,29.155037,28.974243
    ]

    # ok, DCT-RFW
    DCT_RFW_1_100 = [
        40.580210,40.409012,40.676537,41.114418,40.560380,40.413603,39.977345,40.569127,39.816875,43.653979,40.342508,39.845162,40.787647,40.356654,40.459964,40.486738,39.934587,40.206485,40.584806,41.481086,40.384610,40.411877,39.632500,40.368197,41.635355,40.964792,39.962684,40.208164,40.597926,41.600391,42.141057,41.298745,40.732953,41.936896,40.207794,39.933831,40.591683,41.325370,41.031867,40.345847,41.013967,40.992966,40.201511,40.258849,40.200479,40.288361,39.928547,
    ]

    # ok, DKT-RFW
    DKT_RFW_19_128 = [
        42.923157,42.819469,42.987051,42.955971,42.993591,42.792972,42.934846,42.821429,42.736341,43.033412,42.728194,42.920791,42.899255,42.868141,42.944902,42.871057,42.781017,42.856155,42.974770,43.153897,42.854463,42.932991,42.811626,42.834536,42.877121,43.029530,42.891537,42.857400,43.007445,42.981728,43.043536,42.943542,42.846114,43.028497,42.873975,42.784534,42.827247,42.985775,42.904467,42.842246,43.014349,42.862009,42.782186,42.871646,42.864781,42.809031,42.829262,
    ]

    data = [shivani2017, liu2018_k04, DCT_RFW_1_100, DKT_RFW_19_128]

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
    ax1.set_title('Parzival database (47 images)')
    ax1.set_xlabel('Schemes')
    ax1.set_ylabel('PSNR')

    # Now fill the boxes with desired colors
    boxColors = ['darkkhaki', 'green', 'blue', 'red']
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
            '[15]', '[10] k=0.4', 'DCT-RW + FW', 'Krawtchouk-RW + FW'
        ],
        rotation=-20, fontsize=12)
    plt.show()


if __name__ == "__main__":
    run_main()