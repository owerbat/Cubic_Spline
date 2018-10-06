from spline import Spline


def main():
    spline = Spline('dots.txt')
    print(spline.dots, spline.dots_count)
    spline.get_polynomials()
    for el in spline.polynomials:
        print(el)
    spline.get_plot()


main()
