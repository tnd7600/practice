# # Define a generator function
# def my_generator():
#     for i in range(1, 6):
#         yield i


# # Using the generator
# gen = my_generator()


# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


def generator_function():
    yield "First value"
    yield "Second value"
    yield "Third value"


# Calling the generator function
gen = generator_function()

# Iterating through the generator
for value in gen:
    print(value)

# print(next(gen))  # Output: First value
