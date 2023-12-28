from .Figure import *


class Rectangle(Figure):
    def __init__(self, a, b, name, color_transp):
        super().__init__(name, [color_transp[0], color_transp[1]])
        self._a = a
        self._b = b
        self._name = name

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value

    def area(self):
        return self._a * self._b

    def repr(self):
        print("Прямоугольник, сторона a = {}, сторона b = {}, имя: {}, цвет: {}, прозрачность: {}%, площадь S = {}"
              .format(self._a, self._b, self._name, self._color.color, self._color.transparency, self.area()))
