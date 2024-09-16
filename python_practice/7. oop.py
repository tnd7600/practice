# Define a class
class Car:
    # Constructor method to initialize attributes
    def __init__(self, make, model, year):
        self.make = make  # Public attribute
        self.model = model  # Public attribute
        self.year = year  # Public attribute

    # Method to display car details
    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

    # Method to simulate starting the car
    def start(self):
        print(f"{self.make} {self.model} is starting...")

    # Method to simulate stopping the car
    def stop(self):
        print(f"{self.make} {self.model} is stopping...")


# Create an object (instance) of the Car class
my_car = Car("Toyota", "Camry", 2020)
my_car1 = Car("Toyota", "Fortuner - GR Sport variant", 2022)

# Access the object's attributes and methods
print(
    f"My car is a {my_car.year} {my_car.make} {my_car.model}."
)  # Accessing attributes
my_car.display_info()  # Calling method to display information
my_car.start()  # Calling method to start the car
my_car.stop()  # Calling method to stop the car

print(
    f"My car is a {my_car1.year} {my_car1.make} {my_car1.model}."
)  # Accessing attributes
my_car1.display_info()  # Calling method to display information
my_car1.start()  # Calling method to start the car
my_car1.stop()  # Calling method to stop the car

