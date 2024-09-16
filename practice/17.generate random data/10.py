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
