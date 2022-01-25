#상속
class Person(object):
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def about_me(self):
        print("저의 이름은",self.name,"이구요, 제 나이는 ",str(self.age),"살 입니다.")

    def __str__(self):
        return "저의 이름은 {0}입니다. 나이는 {1}살 입니다.".format(
            self.name,self.age
        )

class Korean(Person):
    pass

class Employee(Person):
    def __init__(self,name,age,gender,salary,hire_date):
        super().__init__(name,age,gender)
        self.salary=salary
        self.hire_date=hire_date #속성추가

    #새로운 메서드 추가
    def do_work(self):
        print("열심히 일을 합니다.")

    #부모 클래스 함수 재정의
    def about_me(self):
        super().about_me() #부모 클래스 함수 사용
        print("제 급여는",self.salary,"원 이구요, 제 입사일은 ",self.hire_date,"입니다.")

# first_korean=Korean("Sungchul",35)
# print(first_korean)

myPerson=Person("John",34,"Male")
myPerson.about_me()

myEmployee=Employee("Daeho",34,"Male",300000,"2012/03/01")
myEmployee.about_me()