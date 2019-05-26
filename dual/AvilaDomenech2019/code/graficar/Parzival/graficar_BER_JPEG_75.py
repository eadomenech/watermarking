# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def run_main():
    shivani2017 = [
        0.473725,0.471124,0.483871,0.472425,0.483351,0.487253,0.478148,0.481009,0.485172,0.491155,0.480749,0.485692,0.486733,0.501041,0.473985,
    ]

    # ok
    liu2018_k02 = [
        0.330385,0.326483,0.330645,0.325963,0.328564,0.325182,0.327263,0.327523,0.329605,0.327523,0.328824,0.329344,0.326483,0.329865,0.328824,0.326743,0.327784,0.327003,0.328044,0.325182,0.325963,0.329865,0.325702,0.325442,0.331165,0.327784,0.331165,0.327003,0.331426,0.326483,0.328044,0.327003,0.329084,0.326483,0.328044,0.328564,0.327784,0.327523,0.330905,0.326223,0.329344,0.328824,0.328044,0.329605,0.331165,0.325702,0.329344
    ]

    # ok
    liu2018_k04 = [
        0.333767,0.327784,0.331686,0.332466,0.330905,0.332206,0.330385,0.330905,0.332466,0.332726,0.329084,0.329084,0.331686,0.331426,0.332986,0.330645,0.331686,0.330385,0.330645,0.330125,0.327523,0.329084,0.335588,0.330905,0.331426,0.333767,0.334287,0.333247,0.336108,0.333247,0.331426,0.328304,0.331946,0.330645,0.331946,0.330905,0.327263,0.332726,0.329865,0.330385,0.333767,0.331686,0.336368,0.334807,0.332986,0.329084,0.330905
    ]

    # ok
    liu2018_k08 = [
        0.325182,0.326223,0.327003,0.322320,0.331426,0.335588,0.331946,0.335068,0.331426,0.335328,0.333247,0.338450,0.325182,0.336108,0.335848,0.331686,0.334547,0.332986,0.330645,0.329865,0.331946,0.332986,0.332726,0.329344,0.336368,0.336368,0.337409,0.338189,0.332466,0.335328,0.336108,0.331426,0.340791,0.329344,0.337669,0.331426,0.330125,0.330645,0.329865,0.333247,0.334807,0.334807,0.325182,0.331686,0.332726,0.335328,0.332206
    ]

    # ok
    liu2018_k1 = [
        0.331165,0.330385,0.334807,0.328564,0.334287,0.332206,0.336108,0.335588,0.331946,0.330645,0.330125,0.326743,0.331165,0.332986,0.330645,0.327003,0.331165,0.341051,0.331426,0.330645,0.336108,0.337929,0.330905,0.330905,0.329865,0.336368,0.328564,0.327523,0.339750,0.331426,0.334547,0.332466,0.336368,0.330905,0.330385,0.334807,0.329605,0.327523,0.336108,0.332986,0.336629,0.337929,0.337149,0.332726,0.343132,0.335588,0.335848
    ]

    # ok
    proposed = [
        0.085588,0.073621,0.078824,0.084547,0.082466,0.053590,0.094953,0.091311,0.081686,0.078044,0.074142,0.084287,0.083507,0.082466,0.078564,0.055931,0.070239,0.091051,0.063996,0.086889,0.083247,0.084027,0.082986,0.082986,0.092092,0.067118,0.083507,0.084027,0.081426,0.093392,0.080385,0.065036,0.035900,0.088450,0.084027,0.082726,0.078304,0.083507,0.091571,0.075702,0.077784,0.078044,0.085328,0.086629,0.067898,0.088450,0.088189
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