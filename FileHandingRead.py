# 기본적인 파일 종류는 text/binary 파일로 나눔
# 컴퓨터는 text를 처리하기 위해 binary 파일로 변환
f=open("data/i_have_a_dream.txt","r")
contents=f.read()
print(contents)
f.close()

with open("data/i_have_a_dream.txt","r") as my_file:
    contents2=my_file.read()
    print(type(contents2),contents2)

#한 줄씩 읽어 ListType으로 반환
with open("data/i_have_a_dream.txt","r") as my_file:
    contents3=my_file.readlines() #All File return List
    print(type(contents3)) #type check
    print(contents3) #List Value print

#실행시 마다 한줄식 읽어오기 -> 파일이 너무 커서 메모리에 한번에 올리지 못할때 사용
with open("data/i_have_a_dream.txt","r") as my_file:
    i=0
    while True:
        line=my_file.readline()
        if i==5:
            break
        print("{0} ==== {1}".format(i,line))
        i+=1
line

#단어통계 정보 산출
with open("data/i_have_a_dream.txt","r") as my_file:
    contents4=my_file.read()
    word_list=contents4.split(" ")
    line_list=contents4.split("\n")

print("Total Number of Characters : ",len(contents4))
print("Total Number of Words : ",len(word_list))
print("Total Number of Lines : ",len(line_list))
