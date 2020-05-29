
#파일 쓰기
f = open("count_log.txt", 'w', encoding="utf8")
for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

#글 추가하기
with open("count_log.txt" , 'a', encoding="utf8")as f:
    for i in range(1, 11):
        data = "%d번째 줄입니다.\n" % i
        f.write(data)
f.close()


line_counter = 0
data_header = []
customer_list = []

with open("customers.csv")as customer_data:
    while 1 :
        data = customer_data.readline()
        if not data:
            break
        if line_counter == 0:
            data_header = data.split(",")
        else:
            customer = data.split(",")
            if customer[10].upper() =="USA":
