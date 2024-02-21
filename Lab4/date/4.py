from datetime import datetime, time
def Defference(d2, d1):
    td = d2 - d1
    return td.days * 24 * 3600 + td.seconds
d1 = datetime.strptime('1991-12-16 00:01:02', '%Y-%m-%d %H:%M:%S')
d2 = datetime.now()
print(Defference(d2, d1))