# print reverse of a number

# num = 76542
# print(str(num)[::-1])


num = 76542
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print(reversed_num)
