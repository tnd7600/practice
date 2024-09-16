
num = int(input("Enter a number: "))
num1 = 2
sum=0
for i in range (0,num):
    print(num1,end="+")
    sum += num1 
    num1 = (num1*10)+2
print(" =", sum)

