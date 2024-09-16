# Program to calculate tax

def tax(salary):
    if salary <= 10000:
        tax  = 0
    elif salary <= 20000:
        tax = (salary-10000)*0.1
    else:
        tax = 10000*0.0
        tax += 10000*0.1
        tax += (salary-20000)*0.2
    return tax 


salary = int(input("Enter Your Salary : "))   
print(f"Your  tax is : {tax(salary)}")
