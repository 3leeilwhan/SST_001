import turtle
class Shape:
    """A Shape located at some position (x, y) in the plane"""
    numShapes = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        Shape.numShapes += 1


    def draw(self):
        turtle.penup()
        turtle.setx(self.x)
        turtle.sety(self.y)
        turtle.pendown()

class Circle(Shape):
    """A Circular shape with attributes center position(x, y)"""
    numCircles = 0
    def __init__(self, x, y, radius):
        self.radius = radius
        super().__init__(x, y-radius)
        Circle.numCircles += 1

    def draw(self):
        super().draw()
        turtle.circle(self.radius)

class Rectangle(Shape):
    """A Rectangular shape with attributes position(x, y), width, height"""
    numRectangles = 0
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height
        Rectangle.numRectangles += 1

    def draw(self):
        super().draw()
        for i in range(2):
            turtle.forward(self.width)
            turtle.left(90)
            turtle.forward(self.height)
            turtle.left(90)

class Square(Shape):
    numSquares = 0
    def __init__(self, x, y, length):
        super().__init__(x, y)
        self.length = length
        Square.numSquares += 1

    def draw(self):
        super().draw()
        for i in range(4):
            turtle.forward(self.length)
            turtle.left(90)
