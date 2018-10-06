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
        if self.delta_x == 0:
            return str(round(self.a, 3)) + ' + ' + str(round(self.b, 3)) + 'x + ' + \
                   str(round(self.c, 3)) + 'x^2 + ' + str(round(self.d, 3)) + 'x^3'

        elif self.delta_x > 0:
            if self.a == 0:
                return str(round(self.b, 3)) + '(x-' + str(round(self.delta_x, 3)) + ') + ' + \
                       str(round(self.c, 3)) + '(x-' + str(round(self.delta_x, 3)) + ')^2 + ' +\
                       str(round(self.d, 3)) + '(x-' + str(round(self.delta_x, 3)) + ')^3'
            elif self.b == 0:
                return str(round(self.a, 3)) + ' + ' + str(round(self.c, 3)) + '(x-' + str(round(self.delta_x, 3)) +\
                       ')^2 + ' + str(round(self.d, 3)) + '(x-' + str(round(self.delta_x, 3)) + ')^3'
            elif self.c == 0:
                return str(round(self.a, 3)) + ' + ' + str(round(self.b, 3)) + '(x-' + str(round(self.delta_x, 3)) +\
                       ') + ' + str(round(self.d, 3)) + '(x-' + str(round(self.delta_x, 3)) + ')^3'
            elif self.d == 0:
                return str(round(self.a, 3)) + ' + ' + str(round(self.b, 3)) + '(x-' + str(round(self.delta_x, 3)) +\
                       ') + ' + str(round(self.c, 3)) + '(x-' + str(round(self.delta_x, 3)) + ')^2'
            else:
                return str(round(self.a, 3)) + ' + ' + str(round(self.b, 3)) + '(x-' + str(round(self.delta_x, 3)) + \
                       ') + ' + str(round(self.c, 3)) + '(x-' + str(round(self.delta_x, 3)) +\
                       ')^2 + ' + str(round(self.d, 3)) + '(x-' + str(round(self.delta_x, 3)) + ')^3'

        elif self.delta_x < 0:
            if self.a == 0:
                return str(round(self.b, 3)) + '(x+' + str(round(-self.delta_x, 3)) + ') + ' + \
                       str(round(self.c, 3)) + '(x+' + str(round(-self.delta_x, 3)) + ')^2 + ' +\
                       str(round(self.d, 3)) + '(x+' + str(round(-self.delta_x, 3)) + ')^3'
            elif self.b == 0:
                return str(round(self.a, 3)) + ' + ' + str(round(self.c, 3)) + '(x+' + str(round(-self.delta_x, 3)) +\
                       ')^2 + ' + str(round(self.d, 3)) + '(x+' + str(round(-self.delta_x, 3)) + ')^3'
            elif self.c == 0:
                return str(round(self.a, 3)) + ' + ' + str(round(self.b, 3)) + '(x+' + str(round(-self.delta_x, 3)) +\
                       ') + ' + str(round(self.d, 3)) + '(x+' + str(round(-self.delta_x, 3)) + ')^3'
            elif self.d == 0:
                return str(round(self.a, 3)) + ' + ' + str(round(self.b, 3)) + '(x+' + str(round(-self.delta_x, 3)) +\
                       ') + ' + str(round(self.c, 3)) + '(x+' + str(round(-self.delta_x, 3)) + ')^2'
            else:
                return str(round(self.a, 3)) + ' + ' + str(round(self.b, 3)) + '(x+' + str(round(-self.delta_x, 3)) + \
                       ') + ' + str(round(self.c, 3)) + '(x+' + str(round(-self.delta_x, 3)) +\
                       ')^2 + ' + str(round(self.d, 3)) + '(x+' + str(round(-self.delta_x, 3)) + ')^3'
