from lab_python_oop import *
import matplotlib.pyplot as plt

def main():
    rect1 = Rectangle(10, 12, 'r1', ['black', 50])
    print(rect1.area())
    rect1.repr()
    print('-' * 20)
    circ1 = Circle(10, 'circ1', ['red', 50])
    print(circ1.area())
    circ1.repr()
    print('-' * 20)
    square1 = Square(10, 'Square1', ['white', 50])
    print(square1.area())
    square1.repr()
    print('-' * 20)
    """Тест matplotlib"""
    x = [1, 2, 3, 4, 5]
    y = [25, 32, 34, 20, 25]
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    main()