import datetime

given_date = datetime.datetime(2020, 3, 22, 10, 0, 0)

day=7
hour=12
new_date = given_date + datetime.timedelta(days=day,hours=hour)

print(new_date)

