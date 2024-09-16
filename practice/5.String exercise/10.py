def char_count(str1):
    dict = {}
    for char in str1:
        count = str1.count(char)
        dict[char] = count
    return dict

str1 = "Apple"
print(char_count(str1))
