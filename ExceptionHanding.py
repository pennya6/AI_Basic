#에외처리
a=[1,2,3,4,5]
# for i in range(10):
#     try:
#         print(i,10//i)
#         print(a[i])
#     except ZeroDivisionError:
#         print("ERROR")
#     except IndexError as e:
#         print(e)
#     except Exception as e:
#         print(e)

# for i in range(0,10):
#     try:
#         result=10//i
#     except ZeroDivisionError:
#         print("Not divided by 0")
#     else:
#         print(10//i)
#     finally:
#         print(i,"------",result)

#raise 구문 - 필요에 따라 강제로 Exception 발생
while True:
    value=input("변환할 정수 값을 입력해주세요")
    for digit in value:
        if digit not in "0123456789":
            raise ValueError("숫자값을 입력하지 않았습니다.")
    print("정수값으로 변환된 숫자 - ",int(value))

#assert 구문 - 특정 조건을 만족하지 않을 경우 예외발생
def get_binary_nmuber(decimal_number: int):
    assert isinstance(decimal_number,int) #True, false로 나오고 False이면 코드 멈춤
    return bin(decimal_number)
print(get_binary_nmuber(10))

