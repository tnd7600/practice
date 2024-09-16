class Vehicle:

    def __init__(self, name, max_speed, mileage,colour="white"):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.colour = colour

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.colour, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)