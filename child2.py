from parent1 import rectangle
class parallelepiped(rectangle):
    def __init__(self, h, l, b):
        self.h = h
        self.l = l
        self.b = b

    def volume(self):
        print('volume', (self.h * self.l * self.b))