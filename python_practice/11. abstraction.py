from abc import ABC, abstractmethod


# Abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        self.name = "Animal"
        # return "Unknown sound"
        pass  # Abstract method, no implementation


# Derived class 1
class Dog(Animal):
    def sound(self):
        return "Bark"


# Derived class 2
class Cat(Animal):
    def sound(self):
        return "Meow"


# Creating objects of derived classes
dog = Dog()
cat = Cat()
# name = Animal()

# Accessing the abstract method implemented by derived classes
print(dog.sound())  # Output: Bark
print(cat.sound())  # Output: Meow
# print(name.sound())