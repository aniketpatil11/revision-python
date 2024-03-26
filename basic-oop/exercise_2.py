# car class with color and mileage instances

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
        print(f"The {self.color} car has {self.mileage} miles")
    
    def drive(self, mileage):
        self.mileage = self.mileage + mileage
        print(f"Mileage is {self.mileage}")
    

blue_car = Car("Blue", 20000)
red_car = Car("Red", 30000)


car_mileage = Car("Orange", 0)
car_mileage.drive(100)