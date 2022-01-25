#중간고사 기말고사 점수 따로 받아 저장하는 클래스 구현,
class Score():
    def __init__(self,mid:int,final:int):
        self.__mid=mid
        self.__final=final
    @property
    def mid(self):
        return self.__mid

    @property
    def final(self):
        return self.__final

score=Score(50,75)
print((score.mid+score.final)/2)