import numpy as np

#List와 달리 행과 열 부분을 나눠서 Slicing이 가능하다.
#Matrix의 부분 집합을 추출할 때 유용하다.
a=np.array([[1,2,3,4,5],[6,7,8,9,10]],int)
print(a[:,2:]) #전체 Row의 2열 이상
print(a[1,1:3]) #1 Row의 1열 2열
print(a[1:3]) # 1 Row ~ 2 Row의 전체


#arange - array의 범위를 지정하여 값의 list를 생성하는 명령어
np.arange(30) # range : List의 range와 같은 효과, integer로 0부터 29까지 배열 추출
np.arange(0,5,0.5) #floating poring도 표시가능
np.arange(30).reshape(5,6) #2차원으로 선언

#ones, zeros and empty
#zeros - 0으로 가득한 ndarray 생성
#np.zeros(shape,dtype,order) 형태
np.zeros(shape=(10,),dtype=np.int8) #10 - zero vector 생성
np.zeros((2,5)) #2 by 5 - zero matrix create
#ones - 1로 초기화 된 ndarray 생성
#empty - shape만 주어지고 비어있는 ndarray 생성(memory initalization 이 되어있지 않음)
# -> 메모리 공간만 잡아주는것
# 0으로 안나오고 다른 이상한 값으로 나옴 -> 메모리 공간만 잡은 형태라서 그런것, 즉 값 초기화는 없는 상태
np.empty(shape=(10,),dtype=np.int8)
np.empty((3,5))

#something_like - 기존 ndarray의 shape 크기만큼 1,0 또는 Empty array 반환
test_matrix=np.arange(30).reshape(5,6)
np.ones_like(test_matrix)

#선형대수개념 지원
#identity - 단위 행렬(i 행렬)을 생성한
np.identity(n=3,dtype=np.int8) # n-> number of rows
np.identity(5)

#k의 값의 위치를 지정함
#eye - 대각선인 1인 행렬, k값의 시작 index의 변경이 가능
np.eye(N=3,M=5,dtype=np.int8)
np.eye(3)
np.eye(3,5,k=2) # k-> start index

#diag - 대각 행렬의 값을 추출함
matrix=np.arange(9).reshape(3,3)
np.diag(matrix)
np.diag(matrix,k=1) #k -> start index

# random sampling -  데이터 분포에 따른 sampling으로 array를 생성함
np.random.uniform(0,1,10).reshape(2,5) #균등분포
np.random.normal(0,1,10).reshape(2,5) #정규분포

#계산식 지원
#sum, axis - 축 개념 중요함

#Dot product - basic operation Matrix, dot method use
test_a=np.arange(1,7).reshape(2,3)
test_b=np.arange(7,13).reshape(3,2)
print(test_a.dot(test_b))

