# create a third list which contains only odd from first list and even from second list

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3 = []

print("Element at odd-index positions from list one\n",l1[1::2])
print("Element at even-index positions from list two\n",l2[0::2])

l3.extend(l1[1::2])
l3.extend(l2[0::2])
print("Printing Final third list\n",l3)

