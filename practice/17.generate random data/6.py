
import random
import string

def randomPassword():
    data = string.ascii_letters + string.digits + string.punctuation
    random_password = random.sample(data, 6)
    random_password += random.sample(string.ascii_uppercase, 2)
    random_password += random.choice(string.digits)
    random_password += random.choice(string.punctuation)

    password_list = list(random_password)
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password

print ("Password is ", randomPassword())