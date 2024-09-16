# METHOD 1
tuple1 = (45, 45, 45, 45)
for i in tuple1:
    if tuple1.count(i) == len(tuple1):
        print("True")
        break
else:
    print("False")

# METHOD 2
def check(t):
    return len(set(t))==1

tuple1 = (45, 45, 45, 45)
print(check(tuple1))

# METHOD 3

tuple1 = (45, 45, 45, 45)
print(len(set(tuple1))==1)