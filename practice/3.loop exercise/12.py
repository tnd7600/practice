# print fibonacci series

num = int(input("Enter how many numbers you want in fibonacci series: "))
num1 = 0
num2 = 1

for i in range(1,num+1):
    print(num1)
    fibonacci = num1 + num2
    num1 = num2
    num2 = fibonacci    
