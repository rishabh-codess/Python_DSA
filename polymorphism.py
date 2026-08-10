class Shape:
    def area (self):
        return "the area of the figure"

class Rectangle(Shape):
    
    def __init__ (self, height , width):
        self.height= height
        self.width= width

    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, Radius ):
        self.Radius = Radius
         
    def parameter(self):
        return 2*3.14* self.Radius       
  
def print_area(shape):
    print(f"the area is: {shape.area()}")
def print_parameter(shape):
    print (f"parameter is :{shape.parameter()}")

rectangle =Rectangle(4,5)
circle= Circle(3)  
print_area(rectangle)
print_parameter( circle)