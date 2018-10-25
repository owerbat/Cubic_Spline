import numpy as np
from scipy import interpolate
from matplotlib import pyplot as plt
from spline import Spline


def main():
    spline = Spline('dots.txt')
    print(spline.dots, spline.dots_count)
    spline.get_polynomials()

    x = []
    y = []
    for dot in spline.dots:
        x.append(dot[0])
        y.append(dot[1])
    f = interpolate.interp1d(x, y, kind='cubic')

    xnew = np.arange(min(spline.dots)[0], max(spline.dots)[0], 0.01)
    ynew = f(xnew)
    plt.plot(x, y, 'ro', xnew, ynew)
    plt.grid(True)
    plt.show()


main()
