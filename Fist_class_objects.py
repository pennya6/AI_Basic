#일급함수
def square(x):
    return x*x

def cube(x):
    return x*x*x

def formula(method,argument_list): #함수를 파라미터로 사용
    return [method(value)for value in argument_list]