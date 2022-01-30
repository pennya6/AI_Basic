import numpy as np

# test_array=np.array(["1","4",5,8],float)
# print(test_array)
# print(test_array.dtype)
# print(test_array.shape)

#shape을 아는게 중요하다 크기를 계속 쫒아하는게 중요하다

#shape의 여러가지 정보를 얻는게 ndim & size이다.
#ndim - number of dimension, 텐서의 크기
#size - data의 개수, 전체 데이터의 개수
#nbytes - ndarray object의 메모리 크기를 반환함

#Hading shape 하는 경우는 매우 남ㅎ음
# dimenson을 vector 형태로 변환해야하는 경우도 많이 생길수 있음

#GPU가 좋으면 문제가 없겠지만 그렇지 못한 경우에 Handing shape 하는 경우는 많다.

#일반적으로 데이터 로드후에 y값을 가져올때 vector 형태로 있을텐데 metrix의 형태로 변환하기 위해서 주로 사용
test_matrix=[[1,2,3,4],[1,2,5,8]]
print(np.array(test_matrix).shape)
np.array(test_matrix).reshape(2,2,2)

#y vector -> metrix change code
#-1 : size를 기반으로 row 개수 선정
np.array(test_matrix).reshape(-1,2).shape

#flatten - 다차원 데이터 배열을 1차원 배열로 변환
