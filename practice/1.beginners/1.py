# if multiply is less than 1000 return product else return sum

def calculate(num1,num2):
    if num1*num2 <= 1000:
        product = num1*num2
        return product
    else:
        return num1+num2
    
num1=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
print("The Result is: ",calculate(num1,num2))
