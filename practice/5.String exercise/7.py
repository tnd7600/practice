def balanced(s1, s2):
    result = True
    for i in s1:
        if i in s2:
            continue
        else:
            result = False
    return result        
s1 = "Yn"
s2 = "PYnative"
print(balanced(s1, s2))

s1 = "Ynf"
s2 = "PYnative"
print(balanced(s1, s2))
