class Calculator:
    # Method with default arguments to simulate overloading
    def add(self, a=0, b=0, c=0):
        return a + b + c
    
    def mul(self, a=1, b=1, c=1):
        return a * b * c


# Create an object of the Calculator class
calc = Calculator()

# Call the method with different numbers of arguments
print(calc.add(2, 3))  # Output: 5
print(calc.add(2, 3, 4))  # Output: 9
print(calc.add())  # Output: 0 (no arguments, default values are used)

print(calc.mul(2, 3))  # Output: 6
print(calc.mul(2, 3, 4))  # Output: 24
