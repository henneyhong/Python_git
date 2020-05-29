print("Hello VSCode")

a=1
b=2
c=a+b
print(c)

t=[1,2,3]
a,b,c=t
print(t,a,b,c)

#if
score = 92
if score >=90 :
    print('합격')
else : 
    print('불합격')

#for문

for i in[0,1,2,3,4,5,6,7,8,9,10] : 
    print(i)

for i in range(0,11):
    print(i)

favorite_hobby = ['reading','fishing','shopping']
for hobby in favorite_hobby : 
    print('%s is my favorite hobby' % hobby)

wish_travel_city = {'bankok' : 'Thao','Los Angeles' : 'USA','Manila' : 'Philiphines'}
for city, country in wish_travel_city.items():
    print('%s in %s' % (city,country))

    t=(1,2,3)
    print(t+t,t*2)

for x in range(2,-1,-1):
    print(x)

prices = [2.50, 3.50, 4.50]
for price in prices:
    print('price is',price)

#while문
count = 0
if count < 5:
    print ("Hello, I am an if statement and count is", count)
while count < 5:
    print ("Hello, I am a while and count is", count)
    count += 1

num = 0
while num <= 10:
    if num % 2 == 1:
        print (num)
    num += 1

num = 0
while 1:
    print(num)
    if num == 10:
        break
    num +=1

num = 0
while num < 10:
    num += 1
    if num == 5:
        continue
    print (num)
