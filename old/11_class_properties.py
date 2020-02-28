
"""
Exercise 1

Create a class Rectangle which will be constructed with two values width and height
that the class will store internally.
This class should let the user get the width and the height without being able to set them
Also add a property area that gives the area of the rectangle
"""


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, val):
        if val <= 0:
            print("Your width is incorrect")
        else:
            self._width = val

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, val):
        if val <= 0:
            print("Your height is incorrect")
        else:
            self._height = val

    @property
    def area(self):
        return 2 * (self._width + self._height)


if __name__ == '__main__':
    first_rectangle = Rectangle(1, 2)
    Width = first_rectangle.width
    Height = first_rectangle.height
    print(Width, Height)
    print(first_rectangle.area)
    Width = 4
    Height = 10
    first_rectangle.width = Width
    first_rectangle.height = Height
    print(first_rectangle.width, first_rectangle.height, first_rectangle.area)

