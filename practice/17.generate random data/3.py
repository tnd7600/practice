import secrets

secured = secrets.SystemRandom()
code = secured.randrange(100000,999999)

print(code)


