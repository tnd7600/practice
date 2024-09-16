def middle_Char(str):
    length = len(str)//2
    new_str = str[length-1:length+2]
    return new_str

str1 = "JhonDipPeta"
str2 = "JaSonAy"
print(middle_Char(str1))
print(middle_Char(str2))

