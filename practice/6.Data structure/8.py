# 

number = [47, 64, 69, 37, 76, 83,97]
number2 = number
dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

# method 1
for i in number:
    if i not in dict.values():
        number2.remove(i)
print("after removing unwanted elements from list:",number2)


# method 2
# new_number = []
# for i in number:
#     if i in dict.values():
#         new_number.append(i)
# print("after removing unwanted elements from list:",new_number)

# method 3
# number = [i for i in number if i in dict.values()]
# print("after removing unwanted elements from list:",number)
