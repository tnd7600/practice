class Shape:
    def area(self):
        return "Undefined area"


class Circle(Shape):
    def area(self, radius):
        return 3.14 * radius * radius


class Rectangle(Shape):
    def area(self, length, breadth):
        return length * breadth


# Create objects of Circle and Rectangle
circle = Circle()
rectangle = Rectangle()

# Polymorphism in action
print(circle.area(5))  # Output: 78.5
print(rectangle.area(4, 5))  # Output: 20