#최근에는 pathlib 모듈을 사용해 path를 객체로 다룸
import pathlib

cwd=pathlib.Path.cwd()
print(cwd)
print(cwd.parent)
print(list(cwd.parents))
print(list(cwd.glob("*")))

import os
if not os.path.isdir("test"):
    os.mkdir("test")
if not os.path.exists("test/count_log.txt"):
    f=open("test/count_log.txt","w",encoding="utf8")
    f.write("기록이 시작됩니다.\n")
    f.close()
with open("test/count_log.txt","a",encoding="utf8")as f:
    import random,datetime
    for i in range(1,11):
        stamp=str(datetime.datetime.now())
        value=random.random()*1000000
        log_line=stamp+"\t"+str(value)+"값이 생성되었습니다."+"\n"
        f.write(log_line)