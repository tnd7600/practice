import datetime

date_string = "Feb 25 2020 4:20PM"

date = datetime.datetime.strptime(date_string, "%b %d %Y %I:%M%p")  
#b = month,d=data,y=year,I=hour,M=minute,p=pm
print(date)