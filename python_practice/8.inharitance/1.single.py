# Single Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Animal makes a sound"


class Dog(Animal):  # Single Inheritance: Dog inherits from Animal
    def sound(self):
        return f"{self.name} barks"
    
# Single Inheritance
dog = Dog("Buddy")
print(dog.sound())  # Output: Buddy barks