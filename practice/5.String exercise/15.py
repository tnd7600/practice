import string
str1 = "/*Jon is @developer & musician"

new_str = str1.translate(str.maketrans("", "", string.punctuation))
print(new_str)