from .Rectangle import *


class Square(Rectangle):
    def __init__(self, a, name, color_transp):
        super().__init__(a, a, name, color_transp)
        del self._b

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value

    def area(self):
        return self._a ** 2

    def repr(self):
        print("Квадрат, сторона a = {}, имя: {}, цвет: {}, прозрачность: {}%, площадь S = {}"
              .format(self._a, self._name, self._color.color, self._color.transparency, self.area()))
