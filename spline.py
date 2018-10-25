import numpy as np
from polynom import Polynom
from matplotlib import pyplot as plt


class Spline:
    def __init__(self, file_name):
        try:
            file = open(file_name, 'r', encoding='utf-8')
        except FileNotFoundError:
            print("Dots file is nor founded")
            exit(2)

        self.dots = []
        while True:
            dot = file.readline()
            if len(dot) == 0:
                break
            self.dots.append(dot.split(' '))
        self.dots.sort()
        self.dots_count = len(self.dots)
        self.n = self.dots_count - 1
        file.close()
        for dot in self.dots:
            if len(dot) > 2:
                print("Incorrect file")
                exit(3)
            dot[0] = float(dot[0])
            dot[1] = float(dot[1])

        self.a = np.zeros(self.n)
        self.b = np.zeros(self.n)
        self.c = np.zeros(self.n)
        self.d = np.zeros(self.n)
        self.h = np.zeros(self.n)
        for i in range(self.n):
            self.h[i] = (self.dots[i+1][0] - self.dots[i][0])
        self.polynomials = []

    def get_polynomials(self):
        M = np.zeros((self.n-1, self.n-1))
        M[0][0] = 2*(self.h[0]+self.h[1])
        M[0][1] = self.h[1]
        M[self.n-2, self.n-3] = self.h[self.dots_count-3]
        M[self.n-2, self.n-2] = 2*(self.h[self.n-2]+self.h[self.n-1])
        for i in range(2, self.n-1):
            M[i-1][i-2] = self.h[i-1]
            M[i-1][i-1] = 2*(self.h[i-1]+self.h[i])
            M[i-1][i] = self.h[i]

        v = np.zeros(self.n-1)
        for i in range(1, self.n):
            v[i-1] = 3.0 * ((self.dots[i+1][1] - self.dots[i][1]) / self.h[i] - (self.dots[i][1] - self.dots[i-1][1]) / self.h[i-1])

        result = np.linalg.solve(M, v)
        self.c[0] = 0.0
        for i in range(0, self.n-1):
            self.c[i+1] = result[i]

        for i in range(self.n):
            self.a[i] = self.dots[i][1]

        for i in range(self.n-1):
            self.d[i] = (self.c[i + 1] - self.c[i]) / (3.0 * self.h[i])
            self.b[i] = (self.dots[i+1][1] - self.dots[i][1]) / self.h[i] - \
                        self.h[i] / 3.0 * (self.c[i+1] + 2.0 * self.c[i])
        self.d[self.n-1] = -self.c[self.n-1] / (3.0 * self.h[self.n-1])
        self.b[self.n-1] = (self.dots[self.n][1] - self.dots[self.n-1][1]) / self.h[self.n-1] - \
                           self.h[self.n-1] / 3.0 * 2.0 * self.c[self.n-1]

        self.polynomials = []
        for i in range(self.n):
            self.polynomials.append(Polynom(self.a[i], self.b[i], self.c[i], self.d[i], self.dots[i][0]))

    def get_plot(self):
        plt.figure()
        lag = 0.01
        x_range = []
        y_range = []
        for i in range(self.n):
            x_range.append(np.arange(self.dots[i][0], self.dots[i+1][0] + lag, lag))
            y_range.append(np.array([self.polynomials[i].calculate(el) for el in x_range[i]]))
            plt.plot(x_range[i], y_range[i])
            plt.scatter(self.dots[i][0], self.dots[i][1], color='r')
        plt.scatter(self.dots[self.n][0], self.dots[self.n][1], color='r')
        plt.grid(True)
        plt.show()
