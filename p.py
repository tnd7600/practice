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
from datetime import datetime, timedelta

# Function to generate a random date between two dates
def random_date(start, end):
    # Convert datetime objects to timestamps (seconds since epoch)
    start_timestamp = start.timestamp()
    end_timestamp = end.timestamp()
    
    # Generate a random timestamp between start and end
    random_timestamp = random.uniform(start_timestamp, end_timestamp)
    
    # Convert the random timestamp back to a datetime object
    return datetime.fromtimestamp(random_timestamp)

# Define the start and end dates
d1 = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('1/1/2009 4:50 AM', '%m/%d/%Y %I:%M %p')

# Call the random_date function
print(random_date(d1, d2))