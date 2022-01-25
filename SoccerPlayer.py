#python naming rule
# 함수변수 : camel case, 클래스명 : snake case

#클래스는 __init__ 객체초기화 예약함수 필요

class SoccerPlayer(object):
    #매직메소드
    def __init__(self,name : str,position : str ,back_number : int):
        self.name=name
        self.position=position
        self.back_number=back_number

    def __str__(self):
        return "Hello, My name is %s. My back number is %d" % \
               (self.name,self.back_number)

    def __add__(self, other):
        return self.name+other.name

    #method
    def change_back_number(self,new_number):
        print("선수의 등번호를 변경합니다. : From %d to %d" % (self.back_number,new_number))
        self.back_number=new_number


jinhyun=SoccerPlayer("Jinhyun","MF",10)
jinhyun.change_back_number(5)
print("현재 선수의 등번호는 : ",jinhyun.back_number)