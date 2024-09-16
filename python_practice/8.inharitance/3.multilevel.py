class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Animal makes a sound"
    
class Mammal(Animal):  # Multilevel Inheritance: Mammal inherits from Animal
    def warm_blooded(self):
        return "Mammals are warm-blooded"


class Cow(Mammal):  # Cow inherits from Mammal
    def sound(self):
        return f"{self.name} moos"
    
cow = Cow("Daisy")
print(cow.sound())  # Output: Daisy moos
print(cow.warm_blooded())  # Output: Mammals are warm-blooded