# Hierarchical Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Animal makes a sound"

class Bird(Animal):  # Hierarchical Inheritance: Bird inherits from Animal
    def sound(self):
        return f"{self.name} chirps"


class Eagle(Animal):  # Another Hierarchical Inheritance: Eagle inherits from Animal
    def sound(self):
        return f"{self.name} screeches"

bird = Bird("Tweety")
eagle = Eagle("Hawkeye")
print(bird.sound())  # Output: Tweety chirps
print(eagle.sound())  # Output: Hawkeye screeches