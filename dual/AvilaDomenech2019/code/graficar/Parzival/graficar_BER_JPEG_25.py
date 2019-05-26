# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def run_main():
    shivani2017 = [
        0.476587,0.478408,0.486212,0.478928,0.483871,0.487253,0.493236,0.497919,0.492456,0.494797,0.485692,0.515349,0.504683,0.502862,0.478148,
    ]

    # ok
    liu2018_k02 = [
        0.325963,0.326743,0.330645,0.329344,0.329084,0.328304,0.330125,0.327263,0.327263,0.329865,0.332466,0.326223,0.327263,0.327523,0.328824,0.332206,0.327003,0.324662,0.325182,0.326483,0.326743,0.327523,0.327523,0.329605,0.329344,0.327003,0.328044,0.327523,0.327003,0.325963,0.325442,0.330905,0.329084,0.328304,0.329605,0.324922,0.335328,0.331946,0.330385,0.328564,0.327784,0.328824,0.323881,0.328564,0.328044,0.325442,0.327784
    ]

    # ok
    liu2018_k04 = [
        0.326483,0.327784,0.327263,0.328564,0.325182,0.329084,0.332466,0.326223,0.327003,0.323361,0.329865,0.329084,0.327003,0.331946,0.327003,0.331165,0.327263,0.324142,0.324922,0.329344,0.323881,0.327003,0.326483,0.327523,0.328304,0.325963,0.329605,0.327523,0.329084,0.329865,0.330385,0.328304,0.332466,0.330645,0.329605,0.329865,0.330645,0.331426,0.325182,0.332986,0.328044,0.328564,0.326223,0.326223,0.329084,0.324662,0.327784
    ]

    # ok
    liu2018_k08 = [
        0.323361,0.316597,0.328564,0.328044,0.324922,0.324662,0.326483,0.327523,0.319199,0.330125,0.322320,0.331426,0.325702,0.325442,0.325963,0.327003,0.322841,0.326483,0.324142,0.327784,0.323101,0.329084,0.325182,0.324922,0.321800,0.324142,0.330905,0.319459,0.323361,0.324662,0.329344,0.326743,0.322841,0.324142,0.324402,0.323361,0.324662,0.325702,0.327523,0.327003,0.325702,0.327003,0.325442,0.329865,0.326483,0.327003,0.325963
    ]

    # ok
    liu2018_k1 = [
        0.324922,0.325963,0.325963,0.324142,0.324402,0.328304,0.324662,0.326743,0.321020,0.321540,0.324142,0.324662,0.323101,0.324402,0.327784,0.324922,0.321540,0.324402,0.320499,0.327523,0.325963,0.324662,0.316857,0.330125,0.320760,0.323361,0.321540,0.327003,0.326223,0.325702,0.326743,0.327263,0.328824,0.327523,0.324402,0.325702,0.329084,0.320239,0.324922,0.325182,0.322320,0.330645,0.326483,0.328564,0.326223,0.323881,0.321280
    ]

    # ok
    proposed = [
        0.086368,0.076223,0.079865,0.084807,0.082466,0.055411,0.096514,0.092872,0.082466,0.080125,0.076743,0.086629,0.086889,0.082986,0.080645,0.059313,0.072320,0.093392,0.065297,0.090010,0.085068,0.085848,0.085328,0.084287,0.094433,0.068939,0.086629,0.085588,0.084287,0.092872,0.081946,0.066597,0.037461,0.087669,0.085328,0.085588,0.079865,0.084287,0.092092,0.078564,0.080385,0.079344,0.088710,0.087669,0.069719,0.091051,0.091051
    ]

    data = [shivani2017, liu2018_k02, liu2018_k04, liu2018_k08, liu2018_k1, proposed]

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
    numDists = 6
    boxColors = ['darkkhaki', 'green', 'blue', 'red', '#c586c0', '#ade1f9']
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
            '[9]', '[6] k=0.2', '[6] k=0.4', '[6] k=0.8', '[6] k=1', 'Proposed'
        ],
        rotation=-30, fontsize=12)
    plt.show()


if __name__ == "__main__":
    run_main()