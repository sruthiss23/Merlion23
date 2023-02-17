from parent1 import rectangle
class parallelepiped(rectangle):
    def __init__(self, h, l, b):
        self.h = h
        self.l = l
        self.b = b

    def volume(self):
        print('volume', (self.h * self.l * self.b))


rect = rectangle(2, 4)
rect.area()
rect.perimeter()
r1 = parallelepiped(2, 4, 6)
r1.volume()