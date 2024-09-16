class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Animal makes a sound"

class Pet:
    def type(self):
        return "This is a pet"


class Cat(Animal, Pet):  # Multiple Inheritance: Cat inherits from Animal and Pet
    def sound(self):
        return f"{self.name} meows"

cat = Cat("Whiskers")
print(cat.sound())  # Output: Whiskers meows
print(cat.type())  # Output: This is a pet