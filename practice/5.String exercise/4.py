str1 = "PyNaTive"
new_str = ""
for i in str1:
    if i.islower():
        new_str +=  i
        
for i in str1:
    if i.isupper():
        new_str += i

print(new_str)
