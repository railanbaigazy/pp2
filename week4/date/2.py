import datetime

date = datetime.datetime.now()
yesterday = date - datetime.timedelta(days=1)
tomorrow = date + datetime.timedelta(days=1)

print("Yesterday", yesterday.strftime("%d/%m/%y"))
print("Today", date.strftime("%d/%m/%y"))
print("Tomorrow", tomorrow.strftime("%d/%m/%y"))