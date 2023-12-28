from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, name=None, args=None):
        if args is None:
            args = [None, 0]
        try:
            color, transparency = args
        except ValueError:
            ValueError("Input [color, transparency] in __init__")
        else:
            self._color = Color(color, transparency)
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        self._name = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, args):
        try:
            color, transparency = args
        except ValueError:
            ValueError("Input [color, transparency] in setter")
        else:
            self._color.color = color
            self._color.transparency = transparency

    @abstractmethod
    def area(self):
        pass


class Color:
    def __init__(self, color, transparency):
        self.color = color
        self.transparency = transparency
