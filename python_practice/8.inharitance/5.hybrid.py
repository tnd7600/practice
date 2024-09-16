# Hybrid Inheritance (Combination of Multiple and Multilevel Inheritance)

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Animal makes a sound"

class Pet:
    def type(self):
        return "This is a pet"
    
class Mammal(Animal):  # Multilevel Inheritance: Mammal inherits from Animal
    def warm_blooded(self):
        return "Mammals are warm-blooded"

class Fish(Mammal, Pet):  # Hybrid Inheritance: Fish inherits from Mammal and Pet
    def sound(self):
        return f"{self.name} makes bubble sounds"

fish = Fish("Goldie")
print(fish.sound())  # Output: Goldie makes bubble sounds
print(fish.warm_blooded())  # Output: Mammals are warm-blooded
print(fish.type())  # Output: This is a pet
