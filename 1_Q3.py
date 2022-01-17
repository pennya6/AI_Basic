#각 학생들의 평균점수 구하기
score=[(100,100),(95,90),(55,60),(75,80),(70,70)]
def get_avg(score):
    for i in range(len(score)):
        avg=(score[i][0]+score[i][1])/2
        print(i+1,'번, 평균 : ',avg)
get_avg(score)