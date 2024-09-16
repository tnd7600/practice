try:
    # Example operation: Division by zero
    # result = 10 / 0
    # print(result)

    # Example operation: Accessing an undefined variable
    # print(my_variable)

    # Example operation: Converting an invalid string to an integer
    number = int("invalid_number")

except ZeroDivisionError as zde:
    print(f"Error: Division by zero is not allowed. Details: {zde}")
except NameError as ne:
    print(f"Error: Variable is not defined. Details: {ne}")
except ValueError as ve:
    print(f"Error: Invalid value for conversion. Details: {ve}")
except FileNotFoundError as fnfe:
    print(f"Error: File not found. Details: {fnfe}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Exception handling complete.")


