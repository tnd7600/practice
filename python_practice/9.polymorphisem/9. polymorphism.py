# Parent class
class Animal:
    def sound(self):
        raise NotImplementedError("Subclasses must implement this method")


# Dog class (inherits from Animal)
class Dog(Animal):
    def sound(self):
        return "Bark"


# Cat class (inherits from Animal)
class Cat(Animal):
    def sound(self):
        # super().sound()
        # super().__init__()
        return "Meow"
    
# class Cat1(Animal):
#     def sound(self):
#         super().sound()
#         super().__init__()
#         return "Meow"


# Cow class (inherits from Animal)
class Cow(Animal):
    def sound(self):
        return "Moo"


# Function to demonstrate polymorphism
def animal_sound(animal):
    print(animal.sound())


# Create objects for Dog, Cat, and Cow
dog = Dog()
cat = Cat()
# cat1 = Cat1()
cow = Cow()

# Demonstrating polymorphism using the same method name `sound()`
animal_sound(dog)  # Output: Bark
animal_sound(cat)  # Output: Meow
animal_sound(cow)  # Output: Moo
# animal_sound(cat1)  # Output: Meow