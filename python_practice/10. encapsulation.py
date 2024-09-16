class Employee:
    # Constructor
    def __init__(self, name, age, salary):
        self.name = name  # Public attribute
        self._age = age  # Protected attribute (convention)
        self.__salary = salary  # Private attribute (encapsulation)

    # Public method
    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Age: {self._age}")
        print(f"Salary: {self.__get_salary()}")

    # Private method (accessible only within the class)
    def __get_salary(self):
        return self.__salary

    # Public method to modify the salary
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary amount!")


# Creating an Employee object
emp = Employee("John Doe", 30, 50000)

# Accessing public method
emp.display_info()

# Attempting to access the private attribute directly (will raise AttributeError)
# print(emp.__salary)  # This will raise an error

# Accessing the private attribute via the setter method
emp.set_salary(55000)
emp.display_info()

# Attempting to access private method (will raise AttributeError)
# emp.__get_salary()  # This will raise an error
