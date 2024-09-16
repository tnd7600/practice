# Printing only even index chars in a string

string = input("Enter a string: ")
print(f"Orginal String is  {string} \nPrinting only even index chars")

for i in range(0, len(string), 2):
    print(string[i])

# for i in string:
#     if string.index(i) % 2 == 0:
#         print(i)