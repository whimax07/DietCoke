import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import colorbar, figure, subplot, xlim, ylim

import CircleHelper as cir


def main():
    figure(figsize=(8, 8))
    ax = subplot(aspect='equal')

    # Plot one circle (the biggest one on bottom-right).
    cir.circles(1, 0, 0.5, 'r', alpha=0.2, lw=5, edgecolor='b',
                transform=ax.transAxes)

    # Plot a set of circles (circles in diagonal).
    a = np.arange(11) * 0.3
    xy = np.array([1])
    for i in range(len(a) - 1):
        xy = np.append(xy, xy[i] + (a[i] + a[i + 1]) / (2 * np.sqrt(2)) * 0.8)
    out = cir.circles(xy, xy, a / 2, c=a * 2.5, alpha=1, edgecolor='none')
    colorbar(out)

    xlim(0, 10)
    ylim(0, 10)

    plt.show()


if __name__ == "__main__":
    main()
