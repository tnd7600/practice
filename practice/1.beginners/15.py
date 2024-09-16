# Write a program to calculate power of a number

def power(base,exponent):
    return base**exponent

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

# method 1
print(f"{base} raises to the power of {exponent}: {power(base,exponent)} \ni.e. ({base} *{base} * {base} *{base} *{base} = {power(base,exponent)})")

# method 2
print(f"{base} raises to the power of {exponent}: {base**exponent} \ni.e. ({base} *{base} * {base} *{base} *{base} = {base**exponent})")
