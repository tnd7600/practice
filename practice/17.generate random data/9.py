import random

dice = [1,2,3,4,5,6]

for i in range(5):
    random.seed(30)
    print(random.choice(dice))