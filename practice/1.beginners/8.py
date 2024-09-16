# Print the following pattern
# 1
# 1 2   
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for num in range (1,6):
    for i in range (num):
        print(num, end=" ")
    print()
    