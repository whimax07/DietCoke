import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import colorbar, figure, subplot, xlim, ylim

import CircleHelper as ch


def main():
    figure(figsize=(8, 8))
    ax = subplot(aspect='equal')

    circle0 = [CirclePoints(2)]
    x, y, r, col = addCircle(ax, circle0, 0)

    ch.circles(x, y, r, c=col, edgecolor=None)

    xlim(-5, 5)
    ylim(-5, 5)

    plt.show()


def addCircle(ax, circles, idx):
    x = []
    y = []
    r = []
    col = []
    while idx < 7:
        idx += 1
        circleBack = []
        for circ in circles:
            x.append(circ.Centre[0])
            y.append(circ.Centre[1])
            r.append(circ.Radius)
            col.append(1/idx+300)
            for i in ['n', 'e', 's', 'w']:
                circleBack.append(CirclePoints(circ.Radius / 2,
                                               centre=circ.Corners[i]))
        circles = circleBack
    return x, y, r, col


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
