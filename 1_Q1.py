#홀수데이터만 출력
num_list=[1,5,7,15,16,22,28,29]
def get_odd_num(num_list):
    odd=[]
    for i in range(len(num_list)):
        if num_list[i]%2!=0:
            odd.append(num_list[i])
    return odd
print(get_odd_num(num_list))