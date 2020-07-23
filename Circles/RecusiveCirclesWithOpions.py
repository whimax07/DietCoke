import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import colorbar, figure, subplot, xlim, ylim

import CircleHelper as ch
from APalletColour import *


def main():
    figure(figsize=(8, 8))
    ax = subplot(aspect='equal')

    x = []
    y = []
    r = []
    col = []

    circle0 = [CirclePoints(2)]
    for x_, y_, r_, col_ in addCircle(ax, circle0, 0):
        x.append(x_)
        y.append(y_)
        r.append(r_)
        col.append(col_)

    ch.circles(x[:], y[:], r[:], color=col[:], edgecolor=None)

    xlim(-5, 5)
    ylim(-5, 5)

    plt.show()


def addCircle(ax, circles, idx):
    depth = 7
    col = ColMap(depth)
    while idx < depth:
        idx += 1
        circleBack = []
        for circ in circles:
            # Return the details of the currently made circles.
            yield circ.Centre[0], circ.Centre[1], circ.Radius, col[idx-1]

            # Make new circles.
            edges = ['n', 'e', 's', 'w']
            if idx is not 3:
                for i in edges:
                    circleBack.append(CirclePoints(circ.Radius*3 / 5,
                                                   centre=circ.Corners[i]))
            else:
                circleBack.append(CirclePoints(circ.Radius / 3,
                                               centre=circ.Centre))

        circles = circleBack


def ColMap(depth):
    # colMap = []
    # for i in range(depth):
    #     col = [int(i * 200 / depth) + 120, 0.7, 0.4]
    #     colMap.append(APalletColour(hsl=col).rgb1)
    # return colMap
    colMap = plt.get_cmap('twilight', depth).colors
    return colMap


class CirclePoints(object):
    def __init__(self, radius, centre=[0, 0]):
        super().__init__()
        self.Radius = radius
        self.Centre = centre
        self.Corners = self.Build()

    def Build(self):
        corners = {
            'n': [self.Centre[0], self.Centre[1] + self.Radius],
            'e': [self.Centre[0] + self.Radius, self.Centre[1]],
            's': [self.Centre[0], self.Centre[1] - self.Radius],
            'w': [self.Centre[0] - self.Radius, self.Centre[1]]
        }
        return corners


if __name__ == "__main__":
    main()
