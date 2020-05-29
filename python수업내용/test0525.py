#함수 만들기
def cube(number):
    return number**3
def by_three(number):
    if (number % 3 ==0):
        return cube(number)
    else:
        return False

print (cube(3))

#main 호출

def average(numbers):
    total = 0
    for num in numbers:
        total = total + num

    avg = total/len(numbers)
    return avg

def main() :
    prices = [29, 21, 55, 10]

    result = average(prices)

    print(result)

main()

#파라미터

def connect_URI(server, port):
    str = 'http://' + server + ':' + port
    return str

connect_URI('test.com' , '8080')

connect_URI(port = '8080', server='test.com')

connect_URI('test.com' , port = '8080')

#connect_URI(port='8080' , 'test.com')
#첫번째에 키워드 파라미터를 넣으면 오류남
print(str(connect_URI))
#기본 파라미터 값 지정

def times(a = 10, b = 20):
    return a*b
x = times()
y = times(5)

print(x)
print(y)

#가변 파라미터

# *p : 튜플 타입 파라미터  [p는 임의로 설정하는것 아무거나 해도 상관없음]
# **p : dict type parmeter

def var_param_test(*p):
    return p

a=var_param_test(1,2,3,4,5)

print (a)
print (type(a))

def var_param_test(**p):
    for x,v in p.items():
        print(x,v)
var_param_test (a = 1, b = 2, c = 3, d = 4, e = 5, f = 6)



#리턴 값

def set_value(new_value): 
    x = new_value

retval = set_value(10)
print(retval)


def swap(a,b):
    return b,a
a = swap(1,2)
x, y = swap(1,2)
print(type(a))


#복잡한 수식은 함수로
import math

def get_resul_quadratic_equation(a, b, c):
    values = []
    values.append((-b + math.sqrt(b ** 2 - (4 * a * c)) ) / (2 * a))
    values.append((-b - math.sqrt(b ** 2 - (4 * a * c)) ) / (2 * a))
    return values
print (get_resul_quadratic_equation(1, -2, 1)) 

#pythonic Code
colors = ['red', 'blue', 'green', 'yellow']
result = ' '.join(colors)
print(result)

#split 함수
items = 'zero one two three'.split()
print(items)
langs = 'python,java,javascript'
a,b,c = langs.split(",")
print(langs)
url = 'mail.naver.com'
subdomain,domain,type = url.split('.')
print(url)

#join 함수
result = ''.join(colors)
print(result)

#list comprehension

result = [i for i in range(10)]
print(result)

result = [i for i in range(10) if i % 2 == 0]
print(result)

words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)
stuff = [[w.upper(), w.lower(), len(w)] for w in words]

for i in stuff:
    print(i)

#Enumerate

for i, v in enumerate(['tic','tac','toe']):
    print(i, v)

mylist = ["a","b","c","d"]
print(list(enumerate(mylist)))

{i:j for i,j in enumerate('brown University is an academic institute located in South Korea.' .split())}

#zip

a,b,c = zip((1,2,3), (10,20,30),(100,200,300))
print(a,b,c)

[sum(x) for x in zip((1,2,3), (10,20,30), (100,200,300))]
print (x)
