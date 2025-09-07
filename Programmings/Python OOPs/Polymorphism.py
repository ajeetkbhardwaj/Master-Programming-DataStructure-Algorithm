# Define a parent class
class Shape:
    def area(self):
        pass

# Define child classes that inherit from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Create objects from the child classes
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Treat objects as Shape objects and call the area method
shapes = [circle, rectangle]
for shape in shapes:
    print(shape.area())