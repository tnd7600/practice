# count the number of occurrences of each item in a list

list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
dic = {}
for i in list:
    dic[i] = list.count(i)
print("Printing count of each item ",dic)