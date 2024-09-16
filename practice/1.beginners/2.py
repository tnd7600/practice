#Printing current and previous number sum in a range(10)

p_num = 0
print("Printing current and previous number sum in a range(10)")
for num in range(10):
    print(f"Current Number {num} Previous Number  {p_num}  Sum:  {num+p_num}")
    p_num = num