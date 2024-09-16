# print star pattern

# method 1
# rows = int(input("Enter a number of rows: "))
# for i in range(1,rows+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(rows-1,0,-1):    
#     for j in range(i):
#         print("*",end=" ")
#     print()

# method 2
rows = int(input("Enter a number of rows: "))
for i in range(1,rows+1):
    print("*"* i)
for i in range(rows-1,0,-1):
    print("*"* i)


