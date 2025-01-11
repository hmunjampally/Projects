import calendar

dates = input().split(" ")

month = int(dates[0])
day = int(dates[1])
year = int(dates[2])
week_name = calendar.weekday(year,month,day)
print(calendar.day_name[week_name].upper())