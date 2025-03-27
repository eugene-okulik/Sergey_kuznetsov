import datetime

my_date = "Jan 15, 2023 - 12:05:33"
ph_date = datetime.datetime.strptime(my_date, "%b %d, %Y - %H:%M:%S")
print(ph_date)
print(ph_date.strftime("%d.%m.%Y %H:%M"))
print(ph_date.strftime('%B'))
