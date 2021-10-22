# Python Essential Libraries by Joe Marini course example
# Example file for Pendulum library
from datetime import datetime
import time
import pendulum

# TODO: create a new datetime using pendulum
date1 = pendulum.datetime(2021,10,15,tz="Australia/Sydney")
print(date1)
print(isinstance(date1,datetime))
print(date1.timezone_name)


# TODO: convert the time to another time zone
date2 = date1.in_timezone("Australia/Brisbane")
print(date2)


# TODO: create a new datetime using the now() function
date3 = pendulum.now()
print(date3)
print(date3.timezone.name)

# TODO: Use the local function function
local_date = pendulum.local(2021,10,15)
print(local_date)
print(local_date.timezone_name)

# TODO: Use today, tomorrow, yesterday
today = pendulum.today()
tomorrow = pendulum.tomorrow()
yesterday= pendulum.yesterday() # we can add timezome here as well
print(today)
print(tomorrow)
print(yesterday)


# TODO: create a datetime from a system timestamp
t = time.time()
date4= pendulum.from_timestamp(t)
print(date4)