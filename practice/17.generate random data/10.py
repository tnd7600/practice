
from datetime import datetime
import random

# Parse the two datetime objects
d1 = datetime.strptime("1-1-2023 1:30 PM", "%m-%d-%Y %I:%M %p")
d2 = datetime.strptime("1-1-2024 4:00 PM", "%m-%d-%Y %I:%M %p")

# Convert datetime objects to timestamps (seconds since epoch)
d1_timestamp = d1.timestamp()
d2_timestamp = d2.timestamp()

# Generate a random timestamp between d1 and d2
random_timestamp = random.uniform(d1_timestamp, d2_timestamp)

# Convert the random timestamp back to a datetime object
random_datetime = datetime.fromtimestamp(random_timestamp)

print(random_datetime)



import random
import time

def getRandomDate(start, end ):
    print("Printing random date between", start, " and ", end)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'

    startTime = time.mktime(time.strptime(start, dateFormat))
    endTime = time.mktime(time.strptime(end, dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print ("Random Date = ", getRandomDate("1/1/2016", "12/12/2018")) 
