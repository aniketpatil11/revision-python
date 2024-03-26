# class inheritence 
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age): 
        self.name = name
        self.age = age
    
    def __str__(self):
        # if you want to print print(class) this will work and give the description 
        return f"{self.name} is {self.age} years old"
    
    
    def speak(self, sound): 
        # Error: due to sound 
        return f"{self.name} says {sound}"
    

class GoldenRetriever(Dog):
    def speak(self, sound="Bark"): 
       return super().speak(sound) 
    
golden_retriever_baby = GoldenRetriever("Tommy", 4)
print(golden_retriever_baby.speak())
