#거꾸로 입력된 문자열 역순 출력
sentence="way a is there will a is there where"
def reverse_sentence(sentence):
    list=sentence.split()
    #temp_list=list.reverse()
    #result=' '.join(temp_list)
    return list
print(reverse_sentence(sentence))