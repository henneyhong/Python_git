#튜플
t = (1,2,3)
print (t+t,t*2)
len(t)
t[1]=5

#딕셔너리


#반복
from datetime import datetime as dt
dt.today().year 
bornyear = input("태어난 년도")
year = int(bornyear)
age = dt.today().year - year + 1
if age >= 17 and age < 20 : 
    print("고등학생") 
elif age >=20 and age <27 :
    print("대학생")
else : 
    print("학생아님")
    