# Exercise 1: 

class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
# Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
# Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
lab = Dog("Rocky", 2, "White")
print(lab.name)
print(lab.species)
philo = Dog("Philo", 5, "brown")
print(f"{philo.name}'s coat is {philo.coat_color}")


