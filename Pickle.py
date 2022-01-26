#Pickle - 파이썬의 객체를 영속화하는 built-in 객체
#data, object 등 실행중 정보를 저장 -> 불러와서 사용
#저장해야하는 정보, 계산결과 등 활용이 많음

#객체는 메모리에 있어야함 -> 객체는 인터프리터가 끝나면 사라짐 -> 영속적으로 저장하고 싶을 떄 사용

import pickle
f=open("list.pickle","wb")
test=[1,2,3,4,5]
pickle.dump(test,f)
f.close()

print(test)
del test #삭제

f2=open("list.pickle","rb")
test_pickle=pickle.load(f2)
f2.close()
print(test_pickle)