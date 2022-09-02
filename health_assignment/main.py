
from math import pi
from math import radians


class MyCounter:
    def __init__(self, values):
        self.values = values
        self.count_dict = {}
        self.counter = 0  # this is called a instance variable or field


        for i in values:
            if i in self.count_dict:
                self.count_dict[i] += 1
            else:
                self.count_dict[i] = 1

    def get(self, key):
        if key in self.count_dict:
            return print("{} count for key: {}".format(self.values.count(key), key))

        else:
            return print("{} not found in dictionary".format(key))

    def __str__(self):
        return "Counter Dict: {},  Your text: {}".format(self.count_dict, self.values)



# counter_1 = MyCounter("Hello all")
# counter_1.get("o")
# print(counter_1)

class Shape:
    def area(self):
        return - 1
    def perimeter(self):
        return -1

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.area = Circle.area(self)
        self.perimeter = Circle.perimeter(self)

    def area(self):
        return pi*self.radius**2

    def perimeter(self):
        return 2*pi*self.radius

    def __str__(self):
        print("Circle  __________________________")
        return "Area: {},  Perimeter: {}".format(self.area, self.perimeter)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = Rectangle.area(self)
        self.perimeter = Rectangle.perimeter(self)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2*(self.width + self.height)

    def __str__(self):
        print("Rectangle  __________________________")
        return "Area: {},  Perimeter: {}".format(self.area, self.perimeter)


class Square(Rectangle):
    def __init__(self, width, height):
        super().__init__(width, height)
        return

circle = Circle(15)
print(circle)
rectangle = Rectangle(15,15)
print(rectangle)


