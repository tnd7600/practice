# Print numbers from a list if the number is divisible by 5
   
list = [10, 20, 33, 46, 55]
print(f"Given list is {list}\nDivisible by 5")
for i in list:
    if i % 5 == 0:
        print(i)