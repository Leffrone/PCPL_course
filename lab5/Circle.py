from .Figure import *
from math import pi


class Circle(Figure):
    def __init__(self, r, name, color_transp):
        super().__init__(name, [color_transp[0], color_transp[1]])
        self._r = r

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, value):
        self._r = value

    def area(self):
        return pi * self._r ** 2

    def repr(self):
        print("Круг, радиус r = {}, имя: {}, цвет: {}, прозрачность: {}%, площадь S = {}"
              .format(self._r, self._name, self._color.color, self._color.transparency, self.area()))
