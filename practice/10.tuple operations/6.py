tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = tuple(i for i in tuple1 if i == 44 or i == 55)

print(tuple2)