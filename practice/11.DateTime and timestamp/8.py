from datetime import datetime

given_date = datetime(2020, 2, 25)
date = given_date.strftime("%Y-%m-%d %H:%M:%S")
print(date)
