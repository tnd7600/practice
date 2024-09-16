import datetime

given_date = datetime.datetime(2020, 2, 25)

days_to_remove = 7
new_time = given_date - datetime.timedelta(days=days_to_remove)

print(new_time.date())