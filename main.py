from spline import Spline


def main():
    spline = Spline('dots.txt')
    print(spline.dots, spline.dots_count)
    pol = spline.get_polynomials()
    for el in pol:
        print(el)


main()
