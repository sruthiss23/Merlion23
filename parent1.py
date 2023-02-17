class rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def perimeter(self):
        p = 2 * (self.l + self.b)
        print('perimeter = ', p)

    def area(self):
        a = self.l * self.b
        print('area =', a)