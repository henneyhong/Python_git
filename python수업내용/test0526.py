#class 구현
class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def change_back_number(self, new_number):
        print("선수의 등번호를 변경합니다 : From %d to %d" % (self.back_number, new_number))
        self.back_number = new_number


#    def __init__(self, name, position, back_number):
#        self.name = name
#        self.position = position
#        self.back_number = back_number


 #   def __str__(self):
 #       return "Hello, My name is %s. I play in %s in center"% \
 #       (self.name , self.position)
Jinhyun = SoccerPlayer("Jinhyun", "MF", 10)
print("현재 선수의 등 번호는 : ", Jinhyun.back_number)
Jinhyun.change_back_number(5)
print("현재 선수의 등 번호는 : ", Jinhyun.back_number)

#이차원 리스트 사용하기
names = ["Jin", "Sungchul", "Ronald", "Hong", "Seo"]
positions = ["MF", "DF", "CF", "WF","GK"]
numbers = [10, 15, 20, 3, 1]

players = [[name, position, number ] for name, position , number in zip(names,positions,numbers)]
print(players)
print(players[0])

player_objects = [SoccerPlayer(name, position, number) for name, position, number in zip(names,positions,numbers)]
print(player_objects[0])

#상속
# '''
'''class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def about_me(self):
        print("저의 이름은", self.name, "이구요, 제나이는", str(self.age), "살 입니다.")

 class Employee(Person):
    def __init__(self, name, age, gender, salary, hire_date):
         super().__init__(name, age, gender)
         self.salary = salary
         self.hire_date = hire_date
    def do_work(self):
         print("열심히 일을 합니다.")
    def about_me(self):
        super().about_me()
       print("제 급여는",self.salary, "원 이구요, 제 입사일은 ", self.hire_date, "입니다.")
'''
#다형성
class Animal:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):
    def talk(self):
        return ' MeoW!'
class Dog(Animal):
    def talk(self):
        return ' Woof!Woof! '

animals = [Cat('Nissy'), Cat('Nr.Mistoffees'),Dog('Lassle')]
for animal in animals:
    print(animal.name+ '"'+animal.talk())

    #모듈
    