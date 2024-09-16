str1 = "P@#yn26at^&i5ve"
char= 0
digit = 0
symbol = 0
for i in str1:
    if i.isalpha():
        char += 1
    elif i.isdigit():
        digit += 1
    else:
        symbol +=1

print(f"Total counts of chars, digits, and symbols\n\nchar : {char}\ndigit : {digit}\nsymbol : {symbol}")