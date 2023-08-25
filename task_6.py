class Shape():
    def area(self):
        pass
class Square(Shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side * self.side

class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return 0.5 * self.base *self.height


class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14159 * self.radius * self.radius

def method_overloading(Shape):
    return Shape.area()

square=Square(8)
triangle=Triangle(4,5)
circle=Circle(5)

print("area of the square :",method_overloading(square))
print("area of the triangle :",method_overloading(triangle))
print("area of the circle:",method_overloading(circle))
