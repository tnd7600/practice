import random
import string

def randomString(word):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(word))

print (randomString(5))