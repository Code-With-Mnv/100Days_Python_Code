import datetime as dt

now = dt.datetime.now()  # prints everything.... date and time

year = now.year  # returns year
print(year)

day = now.day
print(day)  # returns day (actually date)

weekday = now.weekday()
print(weekday)

print(now.date())

birthday = dt.datetime(year=2007, month=1, day=8)
print(birthday.date())
