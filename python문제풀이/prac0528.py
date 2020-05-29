import os
import random
from datetime import datetime
import time

for num_a in range(1, 11):
    value = num_a*100000
    value = str(value)
print(value)
timestamp = time.mktime(datetime.today().timetuple())
s = str(timestamp)
print(s)

with open("log\count_log.txt",'w', encoding="utf8")as f:
    f.write(value)
    f.write(s)
f.close()
