
with open("i_have_a_dream.txt","r")as my_file:
    contents = my_file.read()
    print(type(contents).contents)

with open("i_have_a_dream.txt","r") as my_file:
    content_list = my_file.readlines()
    print(type(content_list))
    print(content_list)

with open("i_have_a_dream.txt","r") as my_file:
    i = 0
    while True:
        line = my_file.readline()
        if line.strip() !="":
            print(str(i) + "===" + line.strip())
        if not line:
            break
        i = i + 1


f = open("i_have_a_dream.txt",'r')
char_count = 0
word_count = 0
line_count = 0

for line in f:
    char_count += line.__len__()
    word_count += len(line.split(" "))
    line_count += 1

print("라인 수",line_count)  
print("글자 수",char_count)
print("단어 수",word_count)
f.close()
