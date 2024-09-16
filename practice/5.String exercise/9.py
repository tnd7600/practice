str1 = "PYnative29@#8496"
sum = 0
digits = 0
for i in str1:
    if i.isdigit():
        sum = sum + int(i)
        digits += 1

print(f"Sum is: {sum} Average is  {sum/digits}")