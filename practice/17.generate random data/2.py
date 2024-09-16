import random

list = []
for i in range(100):
    list.append(random.randrange(1000000000,9999999999))

winner = random.sample(list,2)

print(winner)