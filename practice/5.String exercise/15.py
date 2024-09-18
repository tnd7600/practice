import string
str1 = "/*Jon is @developer & musician"

# new_str = str1.translate(str.maketrans("", "", string.punctuation))
# print(new_str)
new_str = ""
for i in str1:
    if i in string.punctuation:
        new_str += "#"
    else:
        new_str += i
print(new_str)