# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def run_main():
    # ok
    DCT_1_100 = [
        40.170868,40.299757,40.348008,40.057077,39.755040,41.515343,40.053122,39.493653,40.210788,39.867095,39.762498,40.819057,40.261005,39.580900,40.268502,39.993451,40.551594,40.112512,39.898899,40.531645,40.501522,41.059768,41.755458,40.851811,40.693769,40.102750,39.759382,39.960968,40.163259,39.613858,39.935454,40.218920,40.990327,39.943143,41.301236,40.112514,39.804522,40.625340,40.384415,40.159426,40.189762,39.706987,40.669905,40.183620,40.396948,39.830450,43.474417,
    ]

    # ok
    DCT_36_90 = [
        40.445678,41.028295,41.245629,40.564365,40.717518,41.948130,40.289249,39.802324,40.613898,40.730317,40.495278,41.770115,40.700222,40.434266,40.196434,40.545332,41.199883,40.613034,40.318271,40.876117,40.709166,41.640611,42.095056,41.663201,41.643830,40.768970,40.606987,40.636520,40.799486,40.574636,40.253386,40.745469,41.722147,40.604836,41.798004,40.634902,40.581612,40.958116,40.558467,40.587722,40.166392,39.892725,41.051083,40.940419,40.415466,40.454171,44.310111,
    ]

    # ok
    proposed = [
        42.986584,42.895992,42.882256,42.683381,42.835921,43.020242,42.924622,42.864412,42.945427,42.854739,42.932375,42.955731,42.931620,42.874809,43.189134,42.865630,42.956634,42.936058,42.881279,42.836930,42.788947,42.932028,42.850779,42.798358,42.858212,43.095764,42.817440,42.928891,42.930049,42.855602,42.986986,42.894890,43.040174,42.868543,42.790990,42.817555,42.933578,42.813403,42.907561,42.966789,43.003232,42.788798,43.002505,42.871044,42.839065,42.840849,42.785617
    ]

    data = [DCT_1_100, DCT_36_90, proposed]

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
    numDists = 3
    boxColors = ['#ade1f9', 'blue', 'red']
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
            'DCT (1, 100)', 'DCT (36, 90)', 'Krawtchouk (19, 128)'
        ],
        rotation=-30, fontsize=12)
    plt.show()


if __name__ == "__main__":
    run_main()