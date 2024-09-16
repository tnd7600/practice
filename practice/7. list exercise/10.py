list1 = [5, 20, 20, 15, 20, 25, 50, 20]

# method 1
def remove_value(list1, val):
    return [i for i in list1 if i!=val]
print(remove_value(list1, 20))

# method 2(a)
new_list1 = [i for i in list1 if i!=20]
print(new_list1)

# method 2(b)
list2 = []
for i in list1:
    if i != 20:
        list2.append(i)
print(list2)

# method 3
while 20 in list1:
    list1.remove(20)
print(list1)

