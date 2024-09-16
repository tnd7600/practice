from datetime import datetime

from dateutil.relativedelta import relativedelta


given_date = datetime(2020, 2, 25).date()

month = 4
new_date = given_date + relativedelta(months=+ month)
print(new_date)
