#File Handing Write
f=open("data/i_have_a_dream.txt","w",encoding="utf8")
for i in range(1,11):
    data="%d번째 줄입니다.\n"%i
    f.write(data)
f.close()

#mode a는 추가모드
with open("data/i_have_a_dream2.txt","a",encoding="utf8") as f:
    for i in range(11,21):
        data="{0}번째 줄입니다.\n".format(i)
        f.write(data)

