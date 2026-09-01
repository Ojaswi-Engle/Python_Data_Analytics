from datetime import date
#today's date
today=date.today()
print(today)

#current time
from datetime import datetime
now=datetime.now().time()
print(now)

#current date+time
from datetime import datetime
dt=datetime.now()
print(dt)

#create date
from datetime import date
d=date(2024,8,12)
print(d)

#create time 
from datetime import time
t=time(3,12,45)
print(t)

#create date+time both
from datetime import datetime
dt=datetime(2005,11,14,5,15,55)
print(dt)

#access day , month ,year ,hour ,min ,sec
from datetime import datetime
dt=datetime(2024,5,12,4,23,12)
print(dt.day)
print(dt.month)
print(dt.year)
print(dt.hour)
print(dt.minute)
print(dt.second)

#compare date
from datetime import date
d1=date(2012,12,2)
d2=date(2012,12,4)
print(d1<d2)

#difference 
diff=d2-d1
print(diff)

#add extra days
from datetime import date,timedelta
today=date.today()
future=today+timedelta(days=4)
print(future)

#add days hours min
from datetime import datetime,timedelta
dt=datetime(2026,12,2)
f=dt+timedelta(days=2,hours=2,minutes=34,seconds=7)
print(f)

#convert date to string (any format)
from datetime import datetime
today=datetime.now()
print(today.strftime('%d-%m-%Y'))

#convert string to date
from datetime import datetime
s='12/09/2023'
print(datetime.strptime(s,'%d/%m/%Y'))


