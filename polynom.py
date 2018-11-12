from numpy import sign as npsign


def sign(value):
    if value < 0:
        return '-'
    elif value > 0:
        return '+'
    else:
        return ''


class Polynom:
    def __init__(self, a=0, b=0, c=0, d=0, delta_x=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.delta_x = delta_x

    def calculate(self, value):
        return self.a + self.b*(value-self.delta_x) + self.c*(value-self.delta_x)**2 + self.d*(value-self.delta_x)**3

    def __str__(self):
        coefs = (self.a, self.b, self.c, self.d)
        result = ''

        for i in range(4):
            if coefs[i] != 0:
                result += sign(coefs[i]) + ' ' + str(abs(round(coefs[i], 3)))
                if i == 0:
                    result += ' '
                elif i == 1:
                    if self.delta_x != 0:
                        result += '(x' + sign(-1 * npsign(self.delta_x)) + str(abs(self.delta_x)) + ') '
                    else:
                        result += 'x '
                else:
                    if self.delta_x != 0:
                        result += '(x' + sign(-1 * npsign(self.delta_x)) + str(abs(self.delta_x)) + ')^' + str(i) + ' '
                    else:
                        result += 'x^' + str(i) + ' '
        return result
