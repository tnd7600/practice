
s1 = "Abc"
s2 = "Xyz"
combine_str = ""

# you can also use variale s1_len and s2_len for length of s1 and s2
# s1_len = len(s1)
# s2_len = len(s2)

s2 = s2[::-1]
max_len = len(s2) if len(s1) > len(s2) else len(s2)

for i in range(max_len):
    if i < len(s1):
        combine_str += s1[i]
    if i < len(s2):
        combine_str += s2[i]
print(combine_str)

