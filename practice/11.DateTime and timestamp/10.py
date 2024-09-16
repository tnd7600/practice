from datetime import datetime

date_1 = datetime(2020, 2, 25)

date_2 = datetime(2020, 9, 17)

day = 0

if date_1 > date_2:
    day = date_1 - date_2
    print(day.days)

else: 
    day = date_2 - date_1
    print(day.days)