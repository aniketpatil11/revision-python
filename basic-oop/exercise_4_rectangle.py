# Rectangle Class: 
class Rectangle:
    def __init__(self, length, width): 
        self.length = length
        self.width = width

    def area(self): 
        return (self.length * self.width)
    
area_of_rect = Rectangle(10, 20)
print(area_of_rect.area())

class Square(Rectangle):
    def __init__(self, side_length):
        return super().__init__(side_length, side_length)
    

aread_of_square = Square(5)
print(aread_of_square.area())