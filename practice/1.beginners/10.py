# take odd from first list and even from second lists and create a new list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
updated_list = []

for i in list1:
    if i % 2 != 0:
        updated_list.append(i)

for i in list2:
    if i % 2 == 0:
        updated_list.append(i)

print(f"result list: {updated_list}")

