# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def run_main():
    # ok
    shivani2017 = [
        37.500297,36.454771,37.282782,37.861082,37.999425,36.537485,37.415230,37.058063,37.709791,37.503477,37.765245,37.551868,38.507642,36.319490,37.649818,39.106791,38.042144,37.440185,38.036023,37.300256,37.602250,37.381033,38.573260,37.742994,37.790639,36.580027,36.900299,37.706166,37.177110,36.599790,39.302258,37.248247,37.617127,37.535052,36.774825,38.110933,38.184961,37.564935,36.606742,37.150987,37.352624,38.471838,37.768990,37.033321,37.094770,37.116407
    ]

    # ok
    liu2018_k04 = [
        32.331859,32.099708,32.047146,32.114249,32.124376,32.117772,32.238632,32.183696,32.291386,32.106276,32.085908,31.915775,32.305541,32.083716,32.096823,32.773287,32.807384,32.375036,32.174672,32.211941,32.312572,32.126755,32.091025,32.391724,32.011642,31.986562,32.220199,32.103485,32.208090,32.253663,32.381753,32.393859,32.396742,32.169662,31.992176,32.184354,32.107401,32.408561,32.039222,32.210420,32.061283,32.193790,32.202004,32.372529,32.298031,32.144885,32.569942,32.013397,32.088313,32.079328,32.543880,31.952614,31.921091,32.474193,32.431124,32.841649,32.388008,32.587619,31.813161,32.163924
    ]

    # ok, DCT-RFW
    DCT_RFW_1_100 = [
        47.623363,47.963179,48.437884,47.927063,47.772461,48.047274,47.914010,48.225578,48.385105,48.078978,47.667210,48.107711,47.985482,48.067957,47.791982,48.041026,47.406239,47.712761,48.152602,48.415464,49.142286,48.236640,48.565803,47.752790,47.900551,48.048373,47.975594,48.130554,48.272352,47.667710,47.979833,48.079709,48.312836,48.014273,48.039560,48.746607,47.507878,48.474371,48.312099,47.920582,47.971391,47.914824,49.036226,47.827011,47.730811,48.062299,48.219326,47.993214,48.073916,47.851610,47.630145,47.909270,48.414982,47.992433,48.111618,48.022762,48.304589,48.020137,48.122412,48.524840,
    ]

    # ok, DKT-RFW
    DKT_RFW_19_128 = [
        47.878285,47.853420,48.046414,47.907034,47.939477,47.735455,47.935446,47.854021,48.042707,48.057450,47.922732,47.890937,48.039144,47.941093,47.888722,48.052789,47.899229,47.838873,47.879789,48.114369,47.995086,47.864612,47.945915,48.057047,47.821185,47.923829,47.894378,47.893424,48.005227,47.908769,47.802983,47.909813,47.961407,48.023033,47.846028,47.950894,47.825479,47.810997,47.854622,47.887811,47.953857,48.050256,48.069505,47.921089,47.801456,47.899878,47.760746,47.884980,47.952854,47.921674,47.749830,47.810677,47.889319,47.923516,47.834536,47.942949,47.874924,47.914484,47.852892,47.995507
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
    ax1.set_title('Saint Gall database (60 images)')
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