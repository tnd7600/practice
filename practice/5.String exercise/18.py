import string

def change_symbol(new_str):
    
    for i in string.punctuation:
        new_str = new_str.replace(i, "#")
    return new_str

str1 = '/*Jon is @developer & musician!!'
print(change_symbol(str1))
