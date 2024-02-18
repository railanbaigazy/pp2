import datetime

date = datetime.datetime.now()
new_date = date - datetime.timedelta(days=5)

print("It was", new_date.strftime("%d/%m/%y 5 days ago"))