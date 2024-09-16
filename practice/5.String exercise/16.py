str1 = 'I am 25 years and 10 months old'
new_str = ""
for i in str1:
    if i.isdigit():
        new_str = new_str+i
print(new_str)
