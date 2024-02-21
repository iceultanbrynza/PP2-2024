import datetime
today = datetime.datetime.now()
yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
print(yesterday, today, tomorrow)