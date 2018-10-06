class Polynom:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def calculate(self, value):
        return self.a + self.b*value + self.c*value**2 + self.d*value**3

    def __str__(self):
        return str(round(self.a, 3)) + ' + ' + str(round(self.b, 3)) + 'x + ' \
               + str(round(self.c, 3)) + 'x^2 + ' + str(round(self.d, 3)) + 'x^3'
