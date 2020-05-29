#입력으로 들어오는 모든 수의 평균 값을 계산해주는 함수
#입력으로 들어오는 수의 개수는 정해지지 않음

def avg_nums(*args):
    result = 0
    for i in args:
        result += 1
    return result/len(args)

#첫번째 항의 값이 0이고 두 번째 항의 값이 1,
#이후에 이어지는 항은 이전의 두 항을 더한 값으로 이루어지는 수열
def fib(n):
    if n < 3:
        return 1
    else :
        return fib(n-1)+fib(n-2)



