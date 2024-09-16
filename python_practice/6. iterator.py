# Define a simple iterator class
class MyNumbers:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= 5:
            current = self.num
            self.num += 1
            return current
        else:
            raise StopIteration


# Create an iterator object
my_numbers = MyNumbers()
my_iter = iter(my_numbers)

# Iterate over the numbers
# for number in my_iter:
#     print(number)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
