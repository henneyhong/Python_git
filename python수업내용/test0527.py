
#예외처리
#try~except
for i in range(10):
    try:
        print(10/i)
    except ZeroDivisionError:
        print("Not divided by 0")

#다른 예외처리 방법
price = input("Enter the price:")
try:
    price = float(price)
    print('price = ', price)
except ValueError:
    print('Not a number!')

price = input("Enter the price:")
try:
    price = float(price)
    print('Price = ', price)
except ValueError as err:
    print(err)

#try~except~else   else: 예외가 발생ㅎ지 않을 때 동작
for i in range(10):
    try:
        result = 10/i
    except ZeroDivisionError:
        print("Not divided by 0")
    else:
        print(10/i)

#try~except~finally  finally: 예외 발생 여부와 상관없이 실행
for i in range(1,10):
    try:
        result = 10//i
        print(result)
    except ZeroDivisionError:
        print("Not divided by 0")
    finally:
        print("종료되었습니다")

#raise

while True:
    value = input("변환할 정수 값을 입력해주세요")
    for digit in value:
        if digit not in "0123456789":
            raise ValueError("숫자값을 입력하지 않으셨습니다")
    print("정수값으로 변환된 숫자 -", int(value))




#사용자 정의 예외 만들기

class BizException(Exception):
    pass

#예외 발생 :raise

try:
    raise BizException('error occurred')
except BizException as e:
    print(e)



#파일 쓰기 읽기
sales_log = open('spam_orders.txt' , 'w')
sales_log.write('The Spam Van')
sales_log.write('Sales Log')

sales_log.close()


f = open("count_log.txt", 'w', encoding = "UTF8")
for i in range(1, 11):
    data = "%d번 째 줄입니다.\n" % i
    f.write(data)
f.close()

with open("count_log.txt" , 'a' , encoding="utf8")as f:
    for i in range(1, 11):
        data = "%d번 째 줄입니다.\n" % i
        f.write(data)
        

