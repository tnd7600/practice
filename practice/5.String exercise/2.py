def add_midd(s1,s2):
    length = len(s1)//2
    new_str = s1[:length] + s2 + s1[length:]
    return new_str
s1 = "Ault"
s2 = "Kelly"

print(add_midd(s1,s2))

