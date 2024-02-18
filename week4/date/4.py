import datetime

def date_difference_sec(date1, date2):
    diff = date2 - date1
    return diff.total_seconds()

date = datetime.datetime.now()
yesterday = date - datetime.timedelta(days=1)
tomorrow = date + datetime.timedelta(days=1)

print("Yesterday", yesterday.strftime("%d/%m/%y"))
print("Today", date.strftime("%d/%m/%y"))
print("Tomorrow", tomorrow.strftime("%d/%m/%y"))

difference = date_difference_sec(yesterday, date)

print(f"Difference between today and yesterday: {difference}s")