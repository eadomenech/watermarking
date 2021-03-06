# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def run_main():
    # ok, DCT-RW
    DCT_RW_1_100 = [
        40.498084,40.352636,41.060767,41.422218,40.349463,40.335919,40.734477,40.897765,39.889893,44.075716,40.515566,40.327129,40.589737,40.348231,40.348673,40.535689,40.433161,40.211666,41.024535,41.015248,40.314940,40.541305,40.039771,40.246275,41.810267,40.674986,40.046358,40.309003,40.554018,41.232950,42.349949,40.871204,40.488072,41.799740,40.345813,39.834985,40.579691,41.364823,41.211247,40.092057,40.836068,41.274622,39.952475,40.221458,40.076532,40.490206,40.324667,
    ]

    # ok, DCT-RFW
    DCT_RFW_1_100 = [
        40.580210,40.409012,40.676537,41.114418,40.560380,40.413603,39.977345,40.569127,39.816875,43.653979,40.342508,39.845162,40.787647,40.356654,40.459964,40.486738,39.934587,40.206485,40.584806,41.481086,40.384610,40.411877,39.632500,40.368197,41.635355,40.964792,39.962684,40.208164,40.597926,41.600391,42.141057,41.298745,40.732953,41.936896,40.207794,39.933831,40.591683,41.325370,41.031867,40.345847,41.013967,40.992966,40.201511,40.258849,40.200479,40.288361,39.928547,
    ]

    # ok, DKT-RW
    DKT_RW_19_128 = [
        43.027396,42.956394,43.081855,43.072000,43.083462,42.945139,43.047888,43.068865,42.937734,43.296780,42.971715,43.099809,43.152016,43.112289,43.027605,43.048282,42.948633,43.050513,43.041730,43.474642,43.015435,43.060335,43.049439,42.959680,43.168210,43.224024,42.967549,43.115914,43.134654,43.063947,43.280562,43.068629,43.011427,43.130041,43.022820,43.084814,42.958041,43.172453,43.071640,43.021719,43.219224,43.117023,42.959648,43.011978,42.971615,42.995635,42.978844,
    ]

    # ok, DKT-RFW
    DKT_RFW_19_128 = [
        42.986584,42.895992,42.882256,42.683381,42.835921,43.020242,42.924622,42.864412,42.945427,42.854739,42.932375,42.955731,42.931620,42.874809,43.189134,42.865630,42.956634,42.936058,42.881279,42.836930,42.788947,42.932028,42.850779,42.798358,42.858212,43.095764,42.817440,42.928891,42.930049,42.855602,42.986986,42.894890,43.040174,42.868543,42.790990,42.817555,42.933578,42.813403,42.907561,42.966789,43.003232,42.788798,43.002505,42.871044,42.839065,42.840849,42.785617
    ]

    data = [
        DCT_RW_1_100, DCT_RFW_1_100, DKT_RW_19_128, DKT_RFW_19_128]

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