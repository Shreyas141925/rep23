from datetime import datetime
from datetime import date
begindate=date.today()
# dates in string format
str_d1 = '2021/10/20'
str_d2 = 

# convert string to date object
d1 = datetime.strptime(str_d1, "%Y/%m/%d")
d2 = datetime.strptime(str_d2, "%Y/%m/%d")

# difference between dates in timedelta
delta = d2 - d1
print(f'Difference is {delta.days} days')
