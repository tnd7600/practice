def f_m_l(s1,s2):
    new_str = s1[0] + s2[0] + s1[len(s1)//2] + s2[len(s2)//2] + s1[-1] + s2[-1]
    return new_str

s1 = "America"
s2 = "Japan"
print(f_m_l(s1,s2))

