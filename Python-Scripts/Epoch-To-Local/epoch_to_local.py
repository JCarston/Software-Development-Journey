import time
import datetime

obj = time.localtime()
now = datetime.datetime.now()
current_time = now.strftime('%Y-%m-%d %H:%M:%S')
print(current_time)
print(obj)