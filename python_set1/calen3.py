from datetime import date
import time
datetoday= date.today()
print("Today's date is", datetoday) 
date1 = date.fromtimestamp(time.time())
print("Date on the given timestamp is ", date1)
