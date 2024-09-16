# print number pattern

rows = int(input("Enter a number of rows: "))

for i in range(rows,0,-1):
    for j in range(i,0,-1):
        print(j, end=" ")
    print()


# while rows>0:
#     j=rows
#     while j>0:
#         print(j, end=" ")
#         j-=1
#     print()
#     rows-=1


# for i in range(1,rows+1):
#     j=rows+1-i
#     while j>0:
#         print(j, end=" ")
#         j-=1
#     print()